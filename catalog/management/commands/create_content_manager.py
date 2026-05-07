from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group


class Command(BaseCommand):
    help = "Create content manager"

    def handle(self, *args, **options):
        moderator_group, created = Group.objects.get_or_create(name='Content Manager')
        change_permission = Permission.objects.get(codename="change_blogarticle")
        moderator_group.permissions.add(change_permission)
        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Content Manager" создана и права настроены'))
        else:
            self.stdout.write(self.style.SUCCESS('Права группы "Content Manager" обновлены'))