from django.conf import settings
from django.db import models
from account.models import User


class Article(models.Model):
    POST_TYPE = [
        ('news', '뉴스'),
        ('ask', 'Ask'),
        ('show', 'Show'),
    ]
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True, null=True)
    like_users = models.ManyToManyField(User, related_name="like_articles") #13열과 15열 기존코드에서는 Article 모델의 author 필드와 like_users 필드가 두번 정의가 되어 > author필드와 like_user필드가 한번만 정의되도록 수정함

    category = models.CharField(
        max_length=10, choices=POST_TYPE, default='news')


    def __str__(self):
        return self.title
