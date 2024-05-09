from django.core.management.base import BaseCommand
from main.models import Data

class Command(BaseCommand):
    help = 'Delete all data from the Food model'

    def handle(self, *args, **kwargs):
        Data.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All data deleted successfully'))