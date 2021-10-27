from django.core.management.base import BaseCommand

from journal import models


class Command(BaseCommand):
    """Lists journal names, codes or domains"""

    help = "Utility to list all of the journal names, codes or domains"

    def add_arguments(self, parser):
        """ Adds arguments to Django's management command-line parser.

        :param parser: the parser to which the required arguments will be added
        :return: None
        """
        parser.add_argument('list_type')
        parser.add_argument('display_type')

    def handle(self, *args, **options):
        list_type = options.get('list_type')
        display_type = options.get('display_type')
        if list_type not in ['names', 'codes', 'domains']:
            print('List Type must be either names, codes or domains')
        elif display_type not in ['one', 'multi']:
            print('Display Type must be one (one line) or multi (multiple lines)')
        else:
            out = []
            for journal in models.Journal.objects.all():
                if list_type == 'names':
                    out.append(journal.name)
                elif list_type == 'domains':
                    out.append(journal.domain)
                else:
                    out.append(journal.code)

            if display_type == 'one':
                string_out = ' '.join(out)
                print(string_out)
            else:
                for line in out:
                    print(line)
