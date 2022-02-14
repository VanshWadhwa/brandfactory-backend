from django.contrib import admin

# Register your models here.
from .models import  newsDataFlips , newsDataNewsApi ,newsDataShorts

# Register your models here.

admin.site.register(newsDataShorts)
admin.site.register(newsDataFlips)
admin.site.register(newsDataNewsApi)
