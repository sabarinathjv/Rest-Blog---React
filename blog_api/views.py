from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response  import Response

# from rest_framework.fields import CurrentUserDefault


#CreateAPIView    only for creation
#ListAPIView   listing the api only 
#ListCreateAPIView creating and listing
#RetrieveAPIView get oly 
#DestroyAPIView  delete only
#UpdateAPIView   do update , but  not accpt blank fields
#RetrieveUpdateAPIView  allow get and update , allows blank firld also
#RetrieveDestroyAPIView  get and delete
#RetrieveUpdateDestroyAPIView  put , get , delete



class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class My_view(APIView):
    # print(a)
    def get(self,request):
        print(request.user)
        return Response({"":""})

