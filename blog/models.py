from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model #or setting.AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def upload_to(instance, filename):
    # return 'posts/{filename}'.format(filename=filename)
    return f'posts/{filename}' 


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)#default value is obj 1
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')#
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager   #call as normal filter in django

    class Meta:
        ordering = ('-published',)  

    def __str__(self):
        return self.title    




class Test(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
   




class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name 



class Product(models.Model):
    name = models.CharField(max_length=255)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



