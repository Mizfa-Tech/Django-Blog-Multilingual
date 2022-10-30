from rest_framework import serializers
from blog.models import Post


class ListPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'slug', 'thumbnail', 'thumbnail_alt',
            'status', 'author', 'category', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at')
