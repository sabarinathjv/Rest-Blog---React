from django.urls import path
from .views import PostList, PostDetail,My_view

app_name = 'blog_api'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('', PostList.as_view(), name='listcreate'),
    path('test', My_view.as_view(), name='test'),
    
]