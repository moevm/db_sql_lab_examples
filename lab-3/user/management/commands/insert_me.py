from django.core.management.base import BaseCommand

from user.models import User


class Command(BaseCommand):
    help = 'Print all users;'

    def handle(self, *args, **options):
        print('Creation of user by username')
        username = input('Input username: ')
        user = User(username=username, email=f'{username}@gmail.com')
        user.save()

        print('Created user:', user.username, user.email, user.role)
