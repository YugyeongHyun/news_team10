from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from article.models import Article
from rest_framework.response import Response
from .serializers import LIKESerializer
from rest_framework import status
from article.serializers import ArticleSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from comment.models import Comment



class LIKEAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.like_users.filter(pk=request.user.pk).exists():
            comment.like_users.remove(request.user)  # 좋아요 취소
        else:
            comment.like_users.add(request.user)  # 좋아요 추가

        serializer = LIKESerializer(comment)
        return Response(serializer.data)


class SearchAPIView(APIView):
    def get(self, request, query):
        articles = Article.objects.filter(title__icontains=query)
        if not articles:
            raise NotFound("검색 결과가 없습니다")

        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    