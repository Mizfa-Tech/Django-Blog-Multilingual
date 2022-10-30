from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from blog.models import Category
from blog.api.serializer import ListCategorySerializer, DetailCategorySerializer, CreateUpdateCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    serializer_class = DetailCategorySerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'slug', 'parent_category', ]
    search_fields = ['title', 'slug', 'parent_category', ]

    def get_queryset(self):
        query = self.model.objects.all()
        return query

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCategorySerializer
        elif self.action in ['create', 'update', 'partial-update']:
            return CreateUpdateCategorySerializer
        return self.serializer_class
