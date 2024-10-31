from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.contrib.auth.hashers import make_password

class CustomUser(models.Model):
    email = models.EmailField(unique=True, validators=[EmailValidator(message="Enter a valid email address")])
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\+?\d{10,15}$', message="Enter a valid phone number")
    ])
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Hash password before saving
        self.password = make_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.email
