from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Import Thailand geography from JSON database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            help='Specify custom database URL',
        )

    def handle(self, *args, **options):
        pass
