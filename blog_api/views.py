from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions

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

#[DjangoModelPermissions]#admin has all the permission , other users only have the permissions we given throrh the admin page based on the model(view,edit,create,delete),or they must be inside a group which has the permission
#[DjangoModelPermissionsOrAnonReadOnly ]combiation of avove and anonyous read acess 


class PostUserWritePermission(BasePermission):#for custom permission
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class PostList(generics.ListCreateAPIView):#test
    permission_classes = [DjangoModelPermissions]#admin can view , add data
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class My_view(APIView):
    # print(a)
    def get(self,request):
        print(request.user)
        return Response({"":""})

