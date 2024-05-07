from django.contrib import admin
from django.urls import path
from . import views
from .views import (LIKEAPIView, SearchAPIView)

app_name = "like"
urlpatterns = [
    path('<str:type>/<int:pk>/like/', LIKEAPIView.as_view(), name='like-toggle'),
    path('search/<str:query>/', SearchAPIView.as_view(), name='article-search'),
]

# path('search/', SearchAPIView.as_view(), name='article-search'),
