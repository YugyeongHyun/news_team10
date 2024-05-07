from rest_framework import serializers
from .models import Article
from comment.serializers import CommentSerializer  # comment 앱에서 Serializer 임포트
from comment.models import Comment

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'created_at', 'updated_at',)

class ArticleDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'comments']

    def get_comments(self, obj):
        # 최상위 댓글만 필터링하여 시리얼라이즈
        comments = Comment.objects.filter(article=obj, parent=None)
        return CommentSerializer(comments, many=True, context={'request': self.context.get('request')}).data