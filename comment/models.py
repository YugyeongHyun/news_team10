from django.db import models
from django.conf import settings
from article.models import Article

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_comments", blank=True)  # 좋아요한 사용자 목록

    def __str__(self):
        return self.title
