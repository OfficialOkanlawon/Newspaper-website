from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveBigIntegerField(null=True, blank=True)
    # country = models.CharField(max_length=40)
    # first_name = models.CharField(null=False, blank=False, max_length=20)

# Create your models here.
