from rest_framework import serializers
from .models import Article
from comment.serializers import CommentSerializer  # comment 앱에서 Serializer 임포트
from comment.models import Comment

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # 사용자 이름을 반환

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'author')
        read_only_fields = ('author',)  # author 필드를 읽기 전용으로 설정

    def create(self, validated_data):
        # 작성자는 요청을 보낸 사용자로 설정
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
class ArticleDetailSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'comments']

    def get_comments(self, obj):
        # 최상위 댓글만 필터링하여 시리얼라이즈
        comments = Comment.objects.filter(article=obj, parent=None)
        return CommentSerializer(comments, many=True, context={'request': self.context.get('request')}).data