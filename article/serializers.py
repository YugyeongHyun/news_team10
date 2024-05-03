from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'created_at',
                  'updated_at',)  # author 포함해야 함


class ArticleDetailSerializer(ArticleSerializer):
    pass
