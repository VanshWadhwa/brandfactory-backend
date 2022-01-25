from django.urls import include, path 
# , re_path
urlpatterns = [
#    re_path(r'^auth/', include('rest_auth.urls')),
#    re_path(r'^auth/register/', include('rest_auth.registration.urls')),
path('auth/', include('rest_auth.urls')),    
path('auth/register/', include('rest_auth.registration.urls'))
]