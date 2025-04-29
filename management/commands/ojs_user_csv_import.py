import csv
import uuid

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction, IntegrityError
from django.utils import timezone

from core.models import AccountRole, Role
from journal.models import Journal

User = get_user_model()

# Map CSV headers to Janeway Role slugs
CSV_ROLE_FIELD_MAP = {
    'Author': 'author',
    'Editor': 'editor',
    'Reviewer': 'reviewer',
    'Copyeditor': 'copyeditor',
    'Production Manager': 'production',
    'Typesetter': 'typesetter',
    'Proofing Manager': 'proofing-manager',
    'Proofreader': 'proofreader',
    'Section Editor': 'section-editor',
}


class Command(BaseCommand):
    help = "Import accounts from a CSV and assign roles."

    def add_arguments(self, parser):
        parser.add_argument(
            '--csv-path',
            required=True,
            help='Path to the CSV file.',
        )
        parser.add_argument(
            '--journal-code',
            required=True,
            help='Code of the journal to assign roles in.',
        )
        parser.add_argument(
            '--activate-accounts',
            action='store_true',
            help='Activate user accounts during import.',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show actions without saving.',
        )

    def handle(self, *args, **options):
        csv_path = options['csv_path']
        journal_code = options['journal_code']
        activate_accounts = options['activate_accounts']
        dry_run = options['dry_run']

        try:
            journal = Journal.objects.get(code=journal_code)
        except Journal.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Journal with code '{journal_code}' does not exist."))
            return

        roles_by_slug = {r.slug: r for r in Role.objects.all()}

        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            mapped_role_fields = {
                field: CSV_ROLE_FIELD_MAP[field]
                for field in reader.fieldnames
                if field in CSV_ROLE_FIELD_MAP
            }

            if dry_run:
                self.stdout.write(self.style.WARNING("Running in dry-run mode. No changes will be saved."))

            for row in reader:
                email = row.get('Email')
                username = row.get('Username') or email

                if not email:
                    self.stderr.write(self.style.ERROR("Row without Email detected; skipping."))
                    continue

                user = None
                created = False

                if dry_run:
                    user_qs = User.objects.filter(email=email)
                    if not user_qs.exists():
                        user_qs = User.objects.filter(username=email)

                    if user_qs.exists():
                        user = user_qs.first()
                        created = False
                    else:
                        self.stdout.write(self.style.NOTICE(f"Would create user: {email}"))
                        continue
                else:
                    try:
                        user, created = User.objects.get_or_create(
                            email=email,
                            defaults={
                                'username': username,
                                'first_name': row.get('First Name', ''),
                                'last_name': row.get('Last Name', ''),
                                'date_joined': timezone.now(),
                                'uuid': uuid.uuid4(),
                                'is_active': activate_accounts,
                            },
                        )
                    except IntegrityError:
                        user_qs = User.objects.filter(email=email)
                        if not user_qs.exists():
                            user_qs = User.objects.filter(username=email)

                        if user_qs.exists():
                            user = user_qs.first()
                            created = False
                        else:
                            self.stderr.write(self.style.ERROR(f"IntegrityError but no matching user found for {email}. Skipping."))
                            continue

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Created user: {email}"))
                else:
                    if activate_accounts and not user.is_active:
                        user.is_active = True
                        if not dry_run:
                            user.save()
                        self.stdout.write(self.style.SUCCESS(f"Activated user: {email}"))

                for csv_field, role_slug in mapped_role_fields.items():
                    if row.get(csv_field, '').strip().lower() == 'yes':
                        role = roles_by_slug.get(role_slug)

                        if role:
                            if dry_run:
                                self.stdout.write(f"Would assign role '{role.name}' to {email}.")
                            else:
                                _, role_created = AccountRole.objects.get_or_create(
                                    user=user,
                                    journal=journal,
                                    role=role,
                                )
                                if role_created:
                                    self.stdout.write(f"Assigned role '{role.name}' to {email}.")

        self.stdout.write(self.style.SUCCESS("Import complete."))
