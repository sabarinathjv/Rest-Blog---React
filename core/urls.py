
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls'),namespace='blog'),
    path('admin/',include('blogapi.urls'),namespace='blog_api'),
]
