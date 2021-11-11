from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views  import APIView
from blog.models import Post
from .serializers import PostSerializer


class PostList(generics.CreateAPIView):
    queryset = Post.postobjects.all()
    print(queryset)
    serializer_class = PostSerializer
    pass


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class My_api(APIView):
    def post(self,request):
        print(Post.postobjects.all())

        return Response({"":""})
