from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def crate_user(self, password, email, **extra_kwargs):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, password, email, **extra_kwargs):
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_staff', True)
        if extra_kwargs.get('is_staff') is not True:
            raise ValueError("The superuser must have is_staff=True")
        if extra_kwargs.get('is_superuser') is not True:
            raise ValueError("Thr superuser must have is_superuser = True")
        return self.CreateUser(email, password, **extra_kwargs)
