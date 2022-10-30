from rest_framework import serializers
from blog.models import Category


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'title', 'slug',
        )
        read_only_fields = ('id', 'created_at', 'updated_at')
