from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group

class Command(BaseCommand):
    help = 'Create group for user'

    def handle(self, *args, **options):
        moderator_group, created = Group.objects.get_or_create(name='Moderator')
        unpublish_permission = Permission.objects.get(codename="can_unpublish_product")
        delete_permission = Permission.objects.get(codename="delete_product")
        moderator_group.permissions.add(unpublish_permission)
        moderator_group.permissions.add(delete_permission)
        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Moderator" создана и права настроены'))
        else:
            self.stdout.write(self.style.SUCCESS('Права группы "Moderator" обновлены'))