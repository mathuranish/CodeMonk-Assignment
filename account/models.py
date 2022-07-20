from time import time
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone

# Create your models here.


class CustomUserManager(BaseUserManager):
    # creating user
    # extrafields come with the default usermodel
    def create_user(self, email, password, **extra_feilds):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_feilds)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_feilds):
        extra_feilds.setdefault("is_staff", True)
        extra_feilds.setdefault("is_superuser", True)

        if extra_feilds.get("is_staff") is False:
            raise ValueError("Superuser has to have is_staff as Ture")

        if extra_feilds.get("is_superuser") is False:
            raise ValueError("Superuser has to have is_superuser as Ture")

        return self.create_user(email=email, password=password, **extra_feilds)


class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=40, unique=True)
    date_of_birth = models.DateField(null=True)
    date_joined = models.DateTimeField(default=timezone.now())
    last_login = models.DateTimeField(default=timezone.now(), verbose_name="last login")

    objects = CustomUserManager()
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
