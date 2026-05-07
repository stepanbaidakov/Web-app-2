from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category

class Command(BaseCommand):
    help = 'Add categories to database'

    Category.objects.all().delete()

    def handle(self, *args, **options):
        call_command('loaddata', 'categories_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded'))