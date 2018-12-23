from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True, default=0) # TDOO validate age >= 18