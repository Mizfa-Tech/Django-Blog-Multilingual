from rest_framework import viewsets

from blog.models import Post
from blog.api.serializer import ListPostSerializer, DetailPostSerializer, CreateUpdatePostSerializer


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    serializer_class = DetailPostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ListPostSerializer
        if self.action == ['create', 'update', 'partial-update']:
            return CreateUpdatePostSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
