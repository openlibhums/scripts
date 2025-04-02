import os
import shutil

from django.core.management.base import BaseCommand
from django.db import transaction

from submission import models as submission_models
from journal import models as journal_models
from core import models as core_models
from identifiers import models as identifiers_models


class Command(BaseCommand):
    help = """
    Copy articles from one journal to another.
    Usage examples:
    python manage.py copy_articles --source=olh --target=alluvium
    python manage.py copy_articles --source=olh --target=alluvium --issue=5
    python manage.py copy_articles --source=olh --target=alluvium --article=123
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '--source',
            required=True,
            help='Source journal code',
        )
        parser.add_argument(
            '--target',
            required=True,
            help='Target journal code',
        )
        parser.add_argument(
            '--issue',
            type=int,
            help='Optional issue ID to filter by',
        )
        parser.add_argument(
            '--article',
            type=int,
            help='Optional single article ID to copy',
        )

    def handle(self, *args, **options):
        source_code = options['source']
        target_code = options['target']
        issue_id = options.get('issue')
        article_id = options.get('article')

        try:
            source_journal = journal_models.Journal.objects.get(code=source_code)
            target_journal = journal_models.Journal.objects.get(code=target_code)
        except journal_models.Journal.DoesNotExist:
            self.stderr.write(self.style.ERROR("One or both journals not found."))
            return

        if article_id:
            articles = submission_models.Article.objects.filter(
                journal=source_journal,
                pk=article_id,
            )
        else:
            articles = submission_models.Article.objects.filter(journal=source_journal)
            if issue_id:
                articles = articles.filter(primary_issue_id=issue_id)

        for article in articles:
            with transaction.atomic():
                self.copy_article(article, target_journal)

    def copy_article(self, article, target_journal):
        new_article = submission_models.Article.objects.get(pk=article.pk)
        new_article.pk = None
        new_article.journal = target_journal

        # Section
        if article.section:
            new_article.section = self.get_or_copy_section(
                article.section,
                target_journal,
            )

        # Licence
        if article.license:
            new_article.license = self.get_or_copy_licence(
                article.license,
                target_journal,
            )

        new_article.save()

        # Issue
        if article.primary_issue:
            new_article.primary_issue = self.get_or_copy_issue(
                article.primary_issue,
                target_journal,
                new_article
            )

        # ManyToMany
        new_article.authors.set(article.authors.all())
        new_article.publisher_notes.set(article.publisher_notes.all())

        # Keywords
        self.copy_keywords(article, new_article)

        # FrozenAuthors
        self.copy_frozen_authors(article, new_article)

        # Files
        self.copy_file_m2m(article, new_article, 'manuscript_files')
        self.copy_file_m2m(article, new_article, 'data_figure_files')
        self.copy_file_m2m(article, new_article, 'source_files')
        self.copy_file_m2m(article, new_article, 'supplementary_files')

        # Images
        new_article.large_image_file = self.copy_file(
            article.large_image_file,
            new_article,
        )
        new_article.thumbnail_image_file = self.copy_file(
            article.thumbnail_image_file,
            new_article,
        )
        new_article.save()

        # Galleys
        self.copy_galleys(article, new_article)

        # Pub ID to link to master record
        self.create_pub_id(article, new_article)

        self.stdout.write(
            self.style.SUCCESS(
                f"Copied article {article.pk} to {new_article.pk} ({new_article.url})")
        )

    def get_or_copy_section(self, section, journal):
        return submission_models.Section.objects.get_or_create(
            journal=journal,
            name=section.name,
            defaults={'sequence': section.sequence},
        )[0]

    def get_or_copy_licence(self, licence, journal):
        return submission_models.Licence.objects.get_or_create(
            journal=journal,
            short_name=licence.short_name,
            defaults={'name': licence.name, 'url': licence.url},
        )[0]

    def get_or_copy_issue(self, issue, journal, targe_article):
        issue_type, c = journal_models.IssueType.objects.get_or_create(
            journal=journal,
            code=issue.issue_type.code,
            defaults={
                'pretty_name': issue.issue_type.pretty_name,
                'custom_plural': issue.issue_type.custom_plural,
            }
        )
        issue, c = journal_models.Issue.objects.get_or_create(
            journal=journal,
            volume=issue.volume,
            issue=issue.issue,
            issue_type=issue_type,
            defaults={
                'date': issue.date,
                'issue_title': issue.issue_title,
            },
        )
        issue.articles.add(targe_article)
        return issue

    def copy_file_m2m(self, source_article, target_article, field_name):
        manager = getattr(source_article, field_name)
        for file in manager.all():
            new_file = self.copy_file(file, target_article)
            if new_file:
                getattr(target_article, field_name).add(new_file)

    def copy_file(self, file, new_article):
        if not file:
            return None

        if file.__class__.__name__ == 'SupplementaryFile':
            original_file = file.file
            new_inner_file = self.copy_file(original_file, new_article)

            new_file = file.__class__.objects.get(pk=file.pk)
            new_file.pk = None
            new_file.file = new_inner_file
            new_file.article_id = new_article.pk
            new_file.save()
            return new_file

        new_file = file.__class__.objects.get(pk=file.pk)
        new_file.pk = None
        new_file.article_id = new_article.pk
        new_file.save()

        if hasattr(file, 'self_article_path'):
            source_path = file.self_article_path()
            target_path = new_file.get_file_path(new_article)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.copy2(source_path, target_path)

        return new_file

    def copy_galleys(self, source_article, target_article):
        for galley in source_article.galley_set.all():
            new_galley = core_models.Galley.objects.get(pk=galley.pk)
            new_galley.pk = None
            new_galley.article = target_article
            new_galley.file = self.copy_file(galley.file, target_article)
            new_galley.css_file = self.copy_file(galley.css_file, target_article)
            new_galley.xsl_file = galley.xsl_file
            new_galley.save()

            for image in galley.images.all():
                copied_image = self.copy_file(image, target_article)
                new_galley.images.add(copied_image)

            new_galley.save()

    def copy_frozen_authors(self, source_article, target_article):
        for fa in source_article.frozenauthor_set.all():
            fa.pk = None
            fa.article = target_article
            fa.save()

    def copy_keywords(self, source_article, target_article):
        target_article.keywords.clear()
        for keyword in source_article.keywords.all():
            target_article.keywords.add(keyword)

    def create_pub_id(self, source_article, target_article):
        pub_id = source_article.pk
        identifiers_models.Identifier.objects.get_or_create(
            id_type='pubid',
            article=target_article,
            identifier=pub_id,
            defaults={
                'enabled': True,
            }
        )
