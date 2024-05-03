from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from article.models import Article
from article.serializers import ArticleDetailSerializer, ArticleSerializer
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
    pass
    # # 권한 미제시

    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(
            article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# comment로 인해 ArticleDetailSerializer 미구현
