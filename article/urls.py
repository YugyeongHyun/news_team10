from django.urls import path
from .views import ArticleListAPIView, ArticleDetailAPIView

app_name = "article"
urlpatterns = [
    path("", ArticleListAPIView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailAPIView.as_view(), name="article_detail"), ]
