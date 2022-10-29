from rest_framework import serializers
from utils.general.models.model_seo_abstract import Seo


class SeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seo
        fields = '__all__'
