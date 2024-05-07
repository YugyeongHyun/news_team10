from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # author =serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Article
        fields = ('title', 'content', 'created_at',
                  'updated_at', 'id', 'url')  # author, url 포함해야 함


class ArticleDetailSerializer(ArticleSerializer):
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'content', 'created_at',
                  'updated_at',)  # comment관련, url, author 누락
