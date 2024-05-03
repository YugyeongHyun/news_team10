from rest_framework import serializers
from .models import Article


class CommentSerializer(serializers.ModelSerializer):
    pass


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'created_at',
                  'updated_at',)  # author, url 포함해야 함


class ArticleDetailSerializer(ArticleSerializer):
    # comment 추가란

    class Meta:
        model = Article
        fields = ('title', 'content', 'created_at',
                  'updated_at',)  # comment관련, url, author 누락
