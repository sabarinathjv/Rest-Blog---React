from django.urls import path
from .views import PostList, PostDetail,My_view,PostListDetailfilter

app_name = 'blog_api'

from rest_framework.routers import DefaultRouter
from .views import PostLists





# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#     path('', PostList.as_view(), name='listcreate'),
#     path('test', My_view.as_view(), name='test'),
    
# ]


# router = DefaultRouter()
# router.register('', PostLists, basename='user')
# urlpatterns = router.urls



urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('mytest', PostList.as_view(), name='listcreate'),
    path('search/', PostListDetailfilter.as_view(), name='test'),
    
]