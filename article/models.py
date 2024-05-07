from django.conf import settings
from django.db import models

# Create your models here.


class Article(models.Model):
    like_users = models.ManyToManyField(
        'auth.User', related_name="like_articles"
    
        
    )
