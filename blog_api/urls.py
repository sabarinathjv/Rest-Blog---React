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

from .views import CreatePost,AdminPostDetail,EditPost,DeletePost

urlpatterns = [
    path('data/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('blogs/', PostList.as_view(), name='listcreate'),
    path('search/', PostListDetailfilter.as_view(), name='test'),
    ###
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
    
]