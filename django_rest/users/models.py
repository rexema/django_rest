from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Man'),
        ('f', 'Woman')
    )
    fio = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDERS)
    email = models.EmailField(unique=True)
