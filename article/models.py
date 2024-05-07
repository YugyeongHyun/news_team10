from django.conf import settings
from django.db import models
from django.conf import settings



class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 작성자 필드 추가
    url = models.URLField(max_length=200, blank=True, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles")

    def __str__(self):
        return self.title
