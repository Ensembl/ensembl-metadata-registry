from rest_framework import serializers
from ensembl_metadata.models.organism import Organism
from ncbi_taxonomy.api.serializers import TaxonomyNodeSerializer


class OrganismSerializer(serializers.ModelSerializer):
    taxon = TaxonomyNodeSerializer(many=False, required=True)

    class Meta:
        model = Organism
        exclude = ['organism_id', 'scientific_name',
                   'taxonomy_id', 'species_taxonomy_id']
