from rest_framework import serializers
from ncbi_taxonomy.models import TaxonomyName, TaxonomyNode


class TaxonomyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxonomyName
        fields = ['taxon_id', 'name_class', 'name']


class TaxonomyNodeSerializer(serializers.ModelSerializer):
    names = TaxonomyNameSerializer(many=True, required=False)
    scientific_name = serializers.SerializerMethodField()

    class Meta:
        model = TaxonomyNode
        fields = ['taxon_id', 'parent_id', 'rank', 'scientific_name', 'names']

    def get_scientific_name(self, obj):
        return TaxonomyName.objects.get(
            taxon_id=obj.taxon_id, name_class='scientific name').name
