from django.core.management.base import BaseCommand
from travel.models import Tourist
import csv

class Command(BaseCommand):
    help = 'Import tourist data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Tourist.objects.create(
                    name=row['title'],
                    description=row['descriptions'],
                    location=row['location'],
                    operating_hours=row['OPERATING_HOURS'],
                    entrance_fee=row['ENTRANCE_FEE'],
                    parking=row['PARKING'],
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported tourist data'))