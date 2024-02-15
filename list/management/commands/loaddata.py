import csv
from django.core.management.base import BaseCommand
from list.models import Data

class Command(BaseCommand):
    help = 'Load data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Data.objects.create(
                    category=row['Category'],
                    description=row['Description'],
                    kilocalories=row['Data.Kilocalories'],
                    protein=row['Data.Protein'],
                    fat=row['Data.Fat.Total Lipid'],
                    carbohydrate=row['Data.Carbohydrate']
                    # Add more fields as needed
                )
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))