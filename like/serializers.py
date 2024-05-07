from rest_framework import serializers
from django.contrib.auth import get_user_model
from article.models import Article
from comment.models import Comment



class LIKESerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'title', 'like_users'] 
