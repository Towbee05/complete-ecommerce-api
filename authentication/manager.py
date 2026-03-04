from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    # **kwargs here represents extra fields 
    def create_user(self, email: str, password: str, **kwargs):
        if not email:
            raise ValueError("A unique email must be provided!!")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email: str, password: str, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is False:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is False:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(email, password, **kwargs)