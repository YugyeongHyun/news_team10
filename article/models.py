from django.conf import settings
from django.db import models
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=100)  # 하이퍼링크로 반환 아직
    content = models. TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True, null=True)
    like_users = models.ManyToManyField(
        'auth.User', related_name="like_articles")
