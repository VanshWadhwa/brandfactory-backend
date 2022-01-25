
from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsDataViews.as_view(), name='news_list'),
]
