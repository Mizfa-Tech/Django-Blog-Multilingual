from rest_framework import viewsets
from blog.models import Category
from blog.api.serializer import ListCategorySerializer, DetailCategorySerializer, CreateUpdateCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    serializer_class = DetailCategorySerializer

    def get_queryset(self):
        query = self.model.objects.all()
        return query

    def get_serializer_class(self):
        if self.action == 'list':
            return ListCategorySerializer
        elif self.action in ['create', 'update', 'partial-update']:
            return CreateUpdateCategorySerializer
        return self.serializer_class
