from rest_framework import serializers
from blog.models import Post
from account.api.serializer import BaseUserSerializer


class CreateUpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'slug', 'content', 'thumbnail', 'thumbnail_alt',
            'status', 'author', 'category'
        )

