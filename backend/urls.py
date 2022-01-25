from django.contrib import admin
from django.urls import include, path
#  , re_path

urlpatterns = [
    
#    re_path(r'^admin/', admin.site.urls),
#    re_path(r'^api/v1/users/',  include('users.urls')),
    
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('posts/', include('post.urls')),
    path('news/', include('newsData.urls')),

]