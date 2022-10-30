from rest_framework import viewsets

from blog.models import Post
from blog.api.serializer import ListPostSerializer


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    serializer_class = ListPostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset
