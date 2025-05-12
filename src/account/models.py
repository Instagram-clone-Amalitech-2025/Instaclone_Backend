from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
import random


class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    REQUIRED_FIELDS = ['email', 'full_name']
    USERNAME_FIELD = 'username'  # or 'email' if using email login


class AuthCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at =models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expires_at

    def generate_auth_code(user):
     code = str(random.randint(100000, 999999))
     expiry = timezone.now() + datetime.timedelta(minutes=5)
    
       
     AuthCode.objects.create(user=user, code=code, expires_at=expiry)

    
    # Send code via email or SMS
    # send_email(user.email, code)

     return code
    
    def verify_auth_code(user, input_code):
     try:
        auth_code = AuthCode.objects.filter(user=user, code=input_code).latest('created_at')
        if auth_code.is_expired():
            return False, "Code expired"
        return True, "Code valid"
     except AuthCode.DoesNotExist:
        return False, "Invalid code"
