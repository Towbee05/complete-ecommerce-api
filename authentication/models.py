from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUserModel(AbstractUser):
    username = None
    email = models.EmailField(verbose_name=_("Email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "users"
        verbose_name_plural = "users"
