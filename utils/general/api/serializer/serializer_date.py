from rest_framework import serializers
from utils.general.models.model_date_abstract import DateBasic


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateBasic
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
