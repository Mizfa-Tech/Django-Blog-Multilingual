from rest_framework import serializers
from blog.models import Post
from account.api.serializer import BaseUserSerializer
from blog.api.serializer.serializer_base_category import BaseCategorySerializer


class ListPostSerializer(serializers.ModelSerializer):
    author = BaseUserSerializer(read_only=True)
    category = BaseCategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'thumbnail', 'thumbnail_alt',
            'status', 'author', 'category', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')
