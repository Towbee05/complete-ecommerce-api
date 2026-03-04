from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUserModel(AbstractUser):
    username = None
    email = models.EmailField(verbose_name=_("Email address"), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = CustomUserManager()

    def __str__(self):
        return self.email