from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from article.models import Article

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        parent_id = self.request.data.get('parent')
        article = None

        if parent_id:
            # 부모 댓글이 지정된 경우 부모 댓글의 article을 사용
            try:
                parent_comment = Comment.objects.get(id=parent_id)
                article = parent_comment.article
            except Comment.DoesNotExist:
                raise ValidationError({'parent': ['Parent comment not found.']})
        else:
            # 부모 댓글이 지정되지 않은 경우 article ID를 요청에서 직접 받음
            article_id = self.request.data.get('article')
            if not article_id:
                raise ValidationError({'article': ['This field is required when no parent is provided.']})
            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotExist:
                raise ValidationError({'article': ['Article not found.']})

        serializer.save(author=self.request.user, article=article)
    
    def get_permissions(self):
        # 'list'와 'retrieve' 액션은 모든 사용자에게 허용, 그 외 액션은 인증된 사용자에게만 허용
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        # 'all_comments' 쿼리 파라미터 또는 특정 작업(수정, 삭제)을 수행할 때 모든 댓글을 반환
        all_comments = self.request.query_params.get('all_comments', 'false').lower() == 'true'
        if all_comments or self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return Comment.objects.all()
        else:
            # 최상위 댓글만 반환
            return Comment.objects.filter(parent=None)
