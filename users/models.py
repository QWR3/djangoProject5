from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, BaseUserManager):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
