from rest_framework import serializers
from .models import Article


# class CommentSerializer(serializers.ModelSerializer):
#     replies = serializers.SerializerMethodField()

#     class Meta:
#         model = Comment
#         fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author', 'parent', 'replies']

#     def get_replies(self, obj):
#         # 대댓글은 'replies' 필드를 통해 직렬화
#         if obj.replies.exists():
#             return CommentSerializer(obj.replies.all(), many=True).data
#         return []

class ArticleSerializer(serializers.ModelSerializer):
    # author =serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = Article
        fields = ('title', 'content', 'created_at',
                  'updated_at', 'id')  # author, url 포함해야 함


class ArticleDetailSerializer(ArticleSerializer):
    # comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ('title', 'content', 'created_at',
                  'updated_at',)  # comment관련, url, author 누락
