import csv
from django.core.management.base import BaseCommand

from stats.models import Match, Deliveries


class Command(BaseCommand):
    help = 'Imports devices from the old database'

    def read_csv_file(self):
        with open(self.file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                print(', '.join(row))

    def save_match(self):
        return True

    def save_deliveries(self):
        return True

    def add_arguments(self, parser):
        parser.add_argument('to_import', type=str)
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        to_import = options.get('to_import')
        self.file_path = options.get('path')
        print("To import", to_import, self.file_path)
        self.read_csv_file()


        # if to_import == 'match':

        # elif to_import == 'deliveries':

