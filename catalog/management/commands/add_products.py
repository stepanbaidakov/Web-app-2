from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product

class Command(BaseCommand):
    help = 'Add products to database'

    Product.objects.all().delete()

    def handle(self, *args, **options):
        call_command('loaddata', 'products_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded'))