
from django.core.management.base import BaseCommand

from user.models import User, Roles


class Command(BaseCommand):
    help = 'Print only active admins'

    def handle(self, *args, **options):
        print('Print only active admin users from database')
        for i, user in enumerate(User.objects.filter(is_active=True, role=Roles.ADMIN)):
            print(f'{i + 1}.', user.username, user.email, user.role, user.is_active)
