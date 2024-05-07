from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:  # Meta 클래스 선언 확인
        model = Comment
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author', 'article', 'parent', 'replies']

    def get_replies(self, obj):
        serializer = CommentSerializer(obj.replies.all(), many=True, context=self.context)
        return serializer.data