from django.contrib.auth.models import AbstractUser
from django.db import models

from roles.models import Role


class User(AbstractUser):
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )