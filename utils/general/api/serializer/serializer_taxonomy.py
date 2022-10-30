from rest_framework import serializers
from utils.general.models.model_taxonomy_abstraction import Taxonomy


class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy
        fields = '__all__'

