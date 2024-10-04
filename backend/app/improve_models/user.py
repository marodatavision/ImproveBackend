# app/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('PREMIUM', 'Premiumnutzer'),
        ('BASIC', 'Basisnutzer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='BASIC')
    preferences = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username