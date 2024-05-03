from django.shortcuts import render
from rest_framework.views import APIView
from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status


class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)  # manu=True
        return Response(serializer.data)

    def post(self, request):
        # 권한 미제시
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # raise_exception
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailAPIView(APIView):
    # 권한 미제시
    pass
