from .views import NewsArticleListView
from django.urls import path

urlpatterns = [
    path('news', NewsArticleListView.as_view(), name='news-article-list'),
    path('news/<int:pk>', NewsArticleListView.as_view(), name='news-article-list/upperlimit'),
]
