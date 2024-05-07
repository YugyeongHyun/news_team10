from rest_framework import serializers
from django.contrib.auth import get_user_model
from article.models import Article


class LIKESerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = all
