from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    REQUIRED_FIELDS = ['email', 'full_name']
    USERNAME_FIELD = 'username'  # or 'email' if using email login


# Create your models here.
