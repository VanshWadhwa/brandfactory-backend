
from django.urls import path
from . import views

urlpatterns = [
    path('shorts/', views.newsDataShortsViews.as_view(), name='news_list-shorts'),
    path('flips/', views.newsDataFlipsViews.as_view(), name='news_list-flips'),

    path('newsApi/', views.newsDataNewsApiViews.as_view(), name='news_list-newsApi'),

]
