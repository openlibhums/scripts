from django.core.management.base import BaseCommand

from review import models as review_models
from journal import models as journal_models
from submission.models import REVIEW_STAGES


class Command(BaseCommand):
    """A management command to clean sections of OJS reviews."""

    help = "Cleans editor text out of OJS reviews."

    def add_arguments(self, parser):
        """ Adds arguments to Django's management command-line parser.

        :param parser: the parser to which the required arguments will be added
        :return: None
        """
        parser.add_argument('journal_code')
        parser.add_argument('separator')
        parser.add_argument('--article_id', default=False)
        parser.add_argument('--dryrun', action="store_true", default=False)

    def handle(self, *args, **options):
        journal_code = options.get('journal_code')
        separator = str(options.get('separator'))
        article_id = options.get('article_id')
        dryrun = options.get('dryrun')

        try:
            journal = journal_models.Journal.objects.get(code=journal_code)
        except journal_models.Journal.objects.DoesNotExist:
            exit('No journal with that code found.')

        review_form_answers = review_models.ReviewAssignmentAnswer.objects.filter(
            assignment__article__journal=journal,
            assignment__article__stage__in=REVIEW_STAGES
        )

        if article_id:
            review_form_answers = review_form_answers.filter(
                assignment__article_id=article_id,
            )

        for review_answer in review_form_answers:
            head, sep, tail = review_answer.answer.partition(separator)
            review_answer.answer = head
            review_answer.assignment.comments_for_editor = tail

            if dryrun and (sep or tail):
                print("Altering answer for article {}, assignment {}. found {}".format(
                    review_answer.assignment.article,
                    review_answer.assignment.pk,
                    separator
                ))
            else:
                review_answer.save()
                review_answer.assignment.save()
