from rest_framework import serializers
from ensembl_metadata.models.genome import \
    Dataset, DatasetDatabase, DatasetStatistic, DatasetRelease, \
    Genome, Bundle, GenomeBundle
from ensembl_metadata.api.assembly.serializers import AssemblySerializer
from ensembl_metadata.api.release.serializers import ReleaseSerializer
from ncbi_taxonomy.api.serializers import TaxonomyNodeSerializer


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


class DatasetReleaseSerializer(serializers.ModelSerializer):
    dataset = DatasetSerializer(many=True, required=True)
    release = ReleaseSerializer(many=True, required=True)

    class Meta:
        model = DatasetRelease
        exclude = ['dataset_release_id']


class GenomeSerializer(serializers.ModelSerializer):
    assembly = AssemblySerializer(many=False, required=True)
    taxon = TaxonomyNodeSerializer(many=False, required=True)
    datasets = DatasetSerializer(many=True, required=False)

    class Meta:
        model = Genome
        exclude = ['genome_id']


class BundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bundle
        exclude = ['bundle_id']


class GenomeBundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeBundle
        exclude = ['genome_bundle_id']
