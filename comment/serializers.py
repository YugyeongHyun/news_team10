from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')  # 사용자 이름을 반환하거나 author 자체를 생략할 수 있습니다.

    class Meta:
        model = Comment
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author', 'article', 'parent', 'replies']

    def get_replies(self, obj):
        serializer = CommentSerializer(obj.replies.all(), many=True, context=self.context)
        return serializer.data
