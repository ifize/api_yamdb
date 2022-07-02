from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = (
    ('user', 'User'),
    ('moderator', 'Moderator'),
    ('admin', 'Admin')
)


class User(AbstractUser):

    email = models.EmailField(
        blank=False,
        max_length=254,
        unique=True
    )
    bio = models.TextField(
        blank=True
    )
    role = models.TextField(
        blank=True,
        choices=ROLES,
        default='user'
    )

    class Meta:
        ordering = ['-id']
