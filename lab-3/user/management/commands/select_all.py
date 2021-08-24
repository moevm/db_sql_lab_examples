from django.core.management.base import BaseCommand

from user.models import User


class Command(BaseCommand):
    help = 'Print all users;'

    def handle(self, *args, **options):
        print('Print all users in database')
        for i, user in enumerate(User.objects.all()):
            print(f'{i + 1}.', user.username, user.email, user.role)
