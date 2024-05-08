from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from article.models import Article
from article.serializers import ArticleDetailSerializer, ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination

class ArticleListAPIView(APIView):
    pagination_class = LimitOffsetPagination
    
    def get(self, request):
        articles = Article.objects.all()
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(articles, request)
        serializer = ArticleSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        # 권한 미제시
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # raise_exception
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


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
