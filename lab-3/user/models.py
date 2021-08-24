from django.db import models
from django.utils.translation import gettext_lazy as _


class Roles(models.TextChoices):
    ADMIN = 'admin', _('admin')
    DEVELOPER = 'developer', _('developer')
    GUEST = 'guest', _('guest')


class User(models.Model):
    username = models.CharField(db_index=True, max_length=255, unique=True, help_text='Username (login)')
    email = models.EmailField(db_index=True, unique=True, help_text='Email of user')

    avatar = models.URLField(help_text='Avatar image', null=True)

    is_active = models.BooleanField(default=True, help_text='Is active user', db_column='isActive')
    is_staff = models.BooleanField(default=False, help_text='Is superuser', db_column='isStaff')

    role = models.CharField(max_length=15, choices=Roles.choices, blank=True, null=True,
                            help_text='Role of user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.username
