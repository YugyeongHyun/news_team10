from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # 클래스 레벨에서 queryset 명시
    serializer_class = CommentSerializer

    def get_queryset(self):
        # 'all_comments' 쿼리 파라미터 또는 특정 작업(수정, 삭제)을 수행할 때 모든 댓글을 반환
        all_comments = self.request.query_params.get('all_comments', 'false').lower() == 'true'
        if all_comments or self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return Comment.objects.all()
        else:
            # 그 외에는 최상위 댓글만 반환
            return Comment.objects.filter(parent=None)

