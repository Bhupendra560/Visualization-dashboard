from django.urls import path
from .views import NewsArticleListView

urlpatterns = [
    path('news/', NewsArticleListView.as_view(), name='news-article-list'),
    path('news/<int:pk>', NewsArticleListView.as_view(), name='news-article-list/upperlimit'),

]