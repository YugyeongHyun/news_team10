from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenBlacklistView,
)
from . import views

app_name = "account"
urlpatterns = [
    path("", views.SignupAPIView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refrsh"),
    path("<str:username>/", views.UserDetailAPIView.as_view(), name="user-detail"),
]
