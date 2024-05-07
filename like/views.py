from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from article.models import Article
from rest_framework.response import Response
from .serializers import LIKESerializer
from rest_framework import status
from article.serializers import ArticleSerializer


class LIKEAPIView(APIView):
    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)  # 좋아요 취소
        else:
            article.like_users.add(request.user)  # 좋아요

        serializer = LIKESerializer(article)
        return Response(serializer.data)


class SearchAPIView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        if query:
            articles = Article.objects.filter(title__icontains=query)
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "검색결과가 없습니다"}, status=status.HTTP_400_BAD_REQUEST)
