from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer

# Create your views here.
class SignupAPIView(APIView):
    def post(self, request):
        data = request.data
        email = data.get("email")
        username = data.get("username")
        
        if not (email and username):
            return Response({"error": "email or username is required"}, status=400)
        
        if get_user_model().objects.filter(email=email).exists():
            return Response({"error": "email exists"}, status=400)
        
        if get_user_model().objects.filter(username=username).exists():
            return Response({"error": "username exists"}, status=400)
        
        user = get_user_model().objects.create_user(
            username=username,
            email=email,
            password=data.get("password"),
            gender=data.get("gender"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            birthdate=data.get("birthdate"),
        )
        return Response(
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            status=201
        )
        
        
class UserDetailAPIView(APIView):
    def get(self, request, username):
        user = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, username):
        user = get_object_or_404(get_user_model(), username=username)
        if request.user != user:
            
            return Response({"error": "permission denied"}, status=403)
        
        serializer = UserSerializer(user, data=request.data, pertial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)