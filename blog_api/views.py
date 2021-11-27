from rest_framework import generics
from rest_framework import viewsets
from blog.models import Post,Test,Product,Tag
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework.permissions import SAFE_METHODS,IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import filters #type 3
from rest_framework.parsers import MultiPartParser, FormParser

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
#[DjangoModelPermissions]#only can see data when logged in ,admin has all the permission , other users only have the permissions we given throrh the admin page based on the model(view,edit,create,delete),or they must be inside a group which has the permission
#[DjangoModelPermissionsOrAnonReadOnly ]combiation of avove and anonyous read acess 

############
#viewsets - provides dry , handle scalable project handling multiple endpoints



class PostUserWritePermission(BasePermission):#for custom permission,returns true 
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

# class PostList(generics.ListCreateAPIView,PostUserWritePermission): # the class based view vary used first
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [PostUserWritePermission]#allow edit and delete by our own post only
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    


################################################ for my testing
class My_view(APIView):

    def get(self,request):
        return Response({"":""})
##################################################        


######################tutorial-4  into to viewset and routers method  1   using viewsets.ViewSet ,  working
# class PostLists(viewsets.ViewSet):#simple type 
#     permission_classes = [AllowAny]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         """
#         This will return list of objects.
#         """
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
 
#     def create(self, request):
#         """
#         This will create an endpoint for POST request.
#         """
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
        
#         return Response(serializer.data)
 
#     def retrieve(self, request, pk=None):
#         """
#         Returns a single object
#         """
#         person = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(person)
#         return Response(serializer_class.data)
 
#     def update(self, request, pk):
#         person = Post.objects.get(pk=pk)
#         serializer = PostSerializer(person, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
 
#         return Response(serializer.data)
 
#     def partial_update(self, request,pk):
#         person = Post.objects.get(pk=pk)
#         serializer = PostSerializer(person, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
 
#         return Response(serializer.data)
 
#     def destroy(self, request,pk):
#         person = Post.objects.get(pk=pk)
#         person.delete()




######################tutorial-4  into to viewset and routers method  2   using ModelViewSet   ,  working


class PostLists(viewsets.ModelViewSet):#these 3 lines do all the operation mentioned above
    permission_classes = [IsAuthenticated] #its enough with the 3 lines , we also has option to override , shown as below
    serializer_class = PostSerializer
    # queryset = Post.postobjects.all()#deafultly have this , can override using get_queryset as below

    # def get_object(self, queryset=None, **kwargs):#filter the post by title ,entered wrong will threw not found
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(Post, title=item)

    def get_object(self, queryset=None, **kwargs):#filter the post by slug , when a post is clicked on home page, individualpost is recieved , when we look the url , the url has the slug,
        item = self.kwargs.get('pk')
        return get_object_or_404(Post,slug=item)

    # Define Custom Queryset , queryset is enough but we can override like this
    def get_queryset(self):
        return Post.objects.all()

##################################################################implementing filter  


class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    

    # def get_queryset(self): #type 1 which hardcode the filtering with id , not here
    #     user = self.request.user
    #     return Post.objects.filter(author=user)

class PostDetail(generics.ListAPIView):
    serializer_class = PostSerializer


    def get_queryset(self):#filter by slug individul #type 2 
        slug = self.kwargs['pk']
        return Post.objects.filter(slug=slug)    

class PostListDetailfilter(generics.ListAPIView):#more advanced
    #api/search/?search=first
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^slug']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.


class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()



###################################333file upload section

class CreatePost(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser] #removing also didt show any error

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








 




