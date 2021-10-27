from django.core.management.base import BaseCommand

from journal import models as journal_models
from utils import setting_handler


class Command(BaseCommand):
    """A management command to update settings."""

    help = "Updates settings for a given set of journals with the provided value."

    def add_arguments(self, parser):
        """ Adds arguments to Django's management command-line parser.

        :param parser: the parser to which the required arguments will be added
        :return: None
        """
        parser.add_argument('setting_group')
        parser.add_argument('setting_name')
        parser.add_argument('-va', '--value')
        parser.add_argument('-c', '--codes',
                            nargs='+',
                            )

    def handle(self, *args, **options):
        setting_group_name = options.get('setting_group')
        setting_name = options.get('setting_name')
        journal_codes = options.get('codes')
        value = options.get('value')

        journals = journal_models.Journal.objects.filter(
            code__in=journal_codes,
        )

        for journal in journals:
            old_setting = setting_handler.get_setting(
                setting_group_name=setting_group_name,
                setting_name=setting_name,
                journal=journal,
                default=True,
            ).processed_value
            setting_handler.save_setting(
                setting_group_name=setting_group_name,
                setting_name=setting_name,
                journal=journal,
                value=value,
            )

            print(
                'Updating {}. Old setting value {}, new setting value {}'.format(
                    journal.name,
                    old_setting,
                    value,
                )
            )


