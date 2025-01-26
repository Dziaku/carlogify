from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, date_of_birth, **extra_fields):
        """
        Create and save a user with the given email, password,
        and date_of_birth.
        """
        if not email:
            raise ValueError("The email adress is required.")
        email = self.normalize_email(email)
        user = self.model(date_of_birth=date_of_birth, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, date_of_birth, **extra_fields):
        """
        Create and save a superuser with the given email, 
        password, and date_of_birth. Extra fields are added
        to indicate that the user is staff, active, and indeed
        a superuser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(email, password, date_of_birth, **extra_fields)
    


class CustomUser(AbstractUser):
    
    username = None
    email = models.EmailField("email adress", unique=True)
    date_of_birth = models.DateField("Date of Birth", null=True)

    USERNAME_FIELD= "email"
    REQUIRED_FIELDS = [
        "date_of_birth",
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    