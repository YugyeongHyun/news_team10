from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER = (
        ("male", "남성"),
        ("female", "여성"),
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    birthdate = models.DateField()
    introduction = models.TextField(default="")