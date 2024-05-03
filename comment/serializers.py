from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author', 'parent', 'replies']

    def get_replies(self, obj):
        # 대댓글은 'replies' 필드를 통해 직렬화
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []
