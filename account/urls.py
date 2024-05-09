from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenBlacklistView,
)
from . import views

app_name= "account"
urlpatterns = [
    path("", views.UserListAPIView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refrsh"),
    path("password/", views.ChangePasswordAPIView.as_view(), name="change_password"),
    path("detail/<str:username>/", views.UserDetailAPIView.as_view(), name="user_detail"),
]
