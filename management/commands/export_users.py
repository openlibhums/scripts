import csv
from collections import defaultdict

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from tqdm import tqdm

from core.models import AccountRole
from journal.models import Journal

User = get_user_model()


def get_user_fields():
    """CSV header -> extractor(user). Add an entry here to export another field."""
    return [
        ("email", lambda user: user.email),
        ("first_name", lambda user: user.first_name),
        ("middle_name", lambda user: user.middle_name),
        ("last_name", lambda user: user.last_name),
        ("salutation", lambda user: user.salutation),
        ("name_prefix", lambda user: user.name_prefix),
        ("suffix", lambda user: user.suffix),
    ]


def build_role_columns(journal):
    """
    Returns (roles_by_user, role_slugs) for a journal.

    role_slugs is every role ever assigned on the journal, active or not,
    so a role doesn't disappear as a column just because nobody active
    currently holds it - a blank column still says the role exists there.
    roles_by_user maps each active user with a role on the journal to the
    set of role slugs they hold there, and drives which rows are written.
    """
    role_slugs = sorted(
        AccountRole.objects.filter(journal=journal)
        .values_list("role__slug", flat=True)
        .distinct()
    )

    roles_by_user = defaultdict(set)
    account_roles = AccountRole.objects.filter(
        journal=journal,
        user__is_active=True,
    ).select_related("user", "role")

    for account_role in account_roles:
        roles_by_user[account_role.user].add(account_role.role.slug)

    return roles_by_user, role_slugs


class Command(BaseCommand):
    help = "Export active user names, emails and roles for a journal to a CSV file."

    def add_arguments(self, parser):
        parser.add_argument(
            "--journal",
            required=True,
            help="Code of the journal to export users for.",
        )
        parser.add_argument(
            "--output-path",
            default="user_export.csv",
            help="Path to write the CSV file to.",
        )

    def handle(self, *args, **options):
        journal_code = options["journal"]
        output_path = options["output_path"]

        try:
            journal = Journal.objects.get(code=journal_code)
        except Journal.DoesNotExist:
            self.stderr.write(self.style.ERROR(f"Journal with code '{journal_code}' does not exist."))
            return

        roles_by_user, role_slugs = build_role_columns(journal)
        user_fields = get_user_fields()
        fieldnames = [header for header, _ in user_fields] + role_slugs

        users = sorted(roles_by_user, key=lambda user: (user.last_name, user.first_name))

        with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for user in tqdm(users, desc="Writing users"):
                row = {header: extractor(user) for header, extractor in user_fields}
                for role_slug in role_slugs:
                    row[role_slug] = "Yes" if role_slug in roles_by_user[user] else ""
                writer.writerow(row)

        self.stdout.write(self.style.SUCCESS(f"Exported user data to {output_path}"))
