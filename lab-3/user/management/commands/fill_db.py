import random

from django.core.management.base import BaseCommand, CommandError

from user.models import User, Roles


class Command(BaseCommand):
    help = 'Fill db sqlite with users.'

    def _create_user(self, i):
        user = User(**{
            'username': f'name_{i}',
            'email': f'sample_{i}_email@gmail.com',
            'avatar': random.choice([
                'https://e7.pngegg.com/pngimages/340/946/png-clipart-avatar-user-computer-icons-software-developer-avatar-child-face.png',
                None]),
            'is_active': random.choice([True, False]),
            'is_staff': random.choice([True, False]),
            'role': random.choice([Roles.ADMIN, Roles.GUEST])
        })
        user.save()

    def handle(self, *args, **options):
        print('Generate 10 random users')
        for i in range(10):
            try:
                self._create_user(i)
            except Exception as e:
                print('Error: ', e)
        print('Generated!')
