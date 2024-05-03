from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from article.models import Article
from rest_framework.response import Response
from .serializers import LIKESerializer


class LIKEAPIView(APIView):
    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)  # 좋아요 취소
        else:
            article.like_users.add(request.user) # 좋아요 
      
        serializer = LIKESerializer(article)
        return Response(serializer.data)
            
            
            
            
            
            
            
    