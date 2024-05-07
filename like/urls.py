from django.contrib import admin
from django.urls import path
from . import views 
from .views import (LIKEAPIView,SearchAPIView)

app_name = "like"
urlpatterns = [
    path('<int:pk>/like/', LIKEAPIView.as_view(), name='like'),
    path('search/', SearchAPIView.as_view(), name='article-search'),
]
