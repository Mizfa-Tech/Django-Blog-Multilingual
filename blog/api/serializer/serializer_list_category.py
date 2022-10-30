from rest_framework import serializers
from blog.models import Category
from blog.api.serializer import BaseCategorySerializer


class ListCategorySerializer(serializers.ModelSerializer):
    parent_category = BaseCategorySerializer(read_only=True)

    class Meta:
        model = Category
        fields = (
            'id', 'title', 'slug', 'thumbnail', 'thumbnail_alt', 'created_at', 'updated_at', 'parent_category'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')
