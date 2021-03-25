from rest_framework import serializers
from ensembl_metadata.models.genome import \
    Organism, OrganismGroup, OrganismGroupMember, \
    Genome, GenomeRelease, \
    Dataset, DatasetDatabase, DatasetStatistic
from ensembl_metadata.api.assembly.serializers import AssemblySerializer
from ensembl_metadata.api.release.serializers import ReleaseSerializer
from ncbi_taxonomy.api.serializers import TaxonomyNodeSerializer


class OrganismSerializer(serializers.ModelSerializer):
    taxon = TaxonomyNodeSerializer(many=False, required=True)

    class Meta:
        model = Organism
        exclude = ['organism_id']


class OrganismGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganismGroup
        exclude = ['organism_group_id']


class OrganismGroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganismGroupMember
        exclude = ['organism_group_member_id']


class DatasetDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetDatabase
        exclude = ['dataset_database_id']


class DatasetStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatasetStatistic
        fields = ('type', 'name', 'value')


class DatasetSerializer(serializers.ModelSerializer):
    dataset_database = DatasetDatabaseSerializer(many=False, required=True)

    class Meta:
        model = Dataset
        exclude = ['dataset_id', 'genome']


class GenomeSerializer(serializers.ModelSerializer):
    assembly = AssemblySerializer(many=False, required=True)
    organism = OrganismSerializer(many=False, required=True)
    datasets = DatasetSerializer(many=True, required=False)

    class Meta:
        model = Genome
        exclude = ['genome_id']


class GenomeReleaseSerializer(serializers.ModelSerializer):
    genome = GenomeSerializer(many=True, required=True)
    release = ReleaseSerializer(many=True, required=True)

    class Meta:
        model = GenomeRelease
        exclude = ['genome_release_id']
