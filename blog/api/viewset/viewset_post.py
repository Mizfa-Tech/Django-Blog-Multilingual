from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from blog.models import Post
from blog.api.serializer import ListPostSerializer, DetailPostSerializer, CreateUpdatePostSerializer


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    lookup_field = 'pk'

    serializer_class = DetailPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title_en', 'title_fa', 'title', ]
    search_fields = ['title', 'category__title', 'author__username', 'author__email', 'slug', 'category__slug']

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return ListPostSerializer
        elif self.action == ['create', 'update', 'partial-update']:
            return CreateUpdatePostSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
