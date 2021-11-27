from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title','category','slug', 'author', 'excerpt','image', 'content', 'status']
        model = Post