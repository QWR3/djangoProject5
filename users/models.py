from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = email
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
