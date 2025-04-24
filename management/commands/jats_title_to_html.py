import os
import traceback
from django.core.management.base import BaseCommand, CommandError
from lxml import etree
from submission.models import Article
from journal.models import Journal, Issue


class Command(BaseCommand):
    help = "Transforms the title field of Articles using an XSLT file. Supports filtering by journal codes, issue IDs, or specific article ID."

    def add_arguments(self, parser):
        parser.add_argument(
            '--journal-codes',
            nargs='+',
            type=str,
            help='Journal codes to filter the articles.',
        )
        parser.add_argument(
            '--article-id',
            type=int,
            help='Specific article ID to process.',
        )
        parser.add_argument(
            '--issue-ids',
            nargs='+',
            type=int,
            help='Issue IDs to filter the articles by associated issues.',
        )
        parser.add_argument(
            '--xslt-file',
            type=str,
            required=True,
            help='Path to the XSLT file to be used for transformation.',
        )
        parser.add_argument(
            '--test-run',
            action='store_true',
            help='Outputs the transformed title without saving.',
        )

    def handle(self, *args, **options):
        journal_codes = options.get('journal_codes')
        article_id = options.get('article_id')
        issue_ids = options.get('issue_ids')
        xslt_file_path = options['xslt_file']
        test_run = options.get('test_run', False)

        if not os.path.exists(xslt_file_path):
            raise CommandError(f"XSLT file not found: {xslt_file_path}")

        with open(xslt_file_path, 'rb') as xslt_file:
            xslt_root = etree.XML(xslt_file.read())
            transform = etree.XSLT(xslt_root)

        if article_id:
            try:
                article = Article.objects.get(id=article_id)
                self.process_article(article, transform, test_run)
            except Article.DoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f'Article with ID "{article_id}" does not exist.'))
            return

        if journal_codes:
            for journal_code in journal_codes:
                try:
                    journal = Journal.objects.get(code=journal_code)
                except Journal.DoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f'Journal with code "{journal_code}" does not exist.'))
                    continue

                articles = Article.objects.filter(journal=journal)

                for article in articles:
                    self.process_article(article, transform, test_run)

        elif issue_ids:
            for issue_id in issue_ids:
                try:
                    issue = Issue.objects.get(id=issue_id)
                except Issue.DoesNotExist:
                    self.stdout.write(self.style.ERROR(
                        f'Issue with ID "{issue_id}" does not exist.'))
                    continue

                for article in issue.articles.all():
                    self.process_article(article, transform, test_run)

        else:
            self.stdout.write(self.style.ERROR(
                'You must provide either --article-id, --journal-codes, or --issue-ids.'))

    def process_article(self, article, transform, test_run):
        try:
            xml_galley = article.xml_galleys.first()
            if not xml_galley:
                self.stdout.write(self.style.WARNING(
                    f'No XML galley found for article ID {article.pk}'))
                return

            file_path = xml_galley.file.get_file_path(article)

            if not os.path.exists(file_path):
                self.stdout.write(self.style.ERROR(
                    f'File path "{file_path}" does not exist for article ID {article.pk}.'))
                return

            with open(file_path, 'rb') as file:
                xml_content = file.read()

            xml_tree = etree.fromstring(xml_content)
            title_element = xml_tree.find('.//title-group/article-title')

            if title_element is None:
                self.stdout.write(self.style.WARNING(
                    f'No article title found in the JATS file for article ID {article.pk}.'))
                return

            transformed_title = transform(title_element)
            title_str = str(transformed_title)

            if test_run:
                self.stdout.write(
                    f'Article PK: {article.pk}\n'
                    f'Old Title: {article.title}\n'
                    f'New Title:\n{title_str.strip()}\n'
                    '----------------------------------------'
                )
            else:
                article.title = title_str.strip()
                article.save()

                self.stdout.write(self.style.SUCCESS(
                    f'Successfully transformed title for article ID {article.pk}'))

        except etree.XMLSyntaxError as e:
            self.stdout.write(self.style.ERROR(
                f'XML syntax error for article ID {article.pk}: {e}\n{traceback.format_exc()}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f'Error processing article ID {article.pk}: {e}\n{traceback.format_exc()}'))
