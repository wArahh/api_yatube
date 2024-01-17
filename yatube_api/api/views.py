from rest_framework import viewsets

from posts.models import Group, Post, Comment

from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer