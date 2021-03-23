from rest_framework import serializers
from ensembl_metadata.api.assembly.serializers import AssemblySerializer
from ensembl_metadata.api.organism.serializers import OrganismSerializer
from ensembl_metadata.models.genome import \
    Division, Genome, GenomeAlignment, GenomeAnnotation, GenomeComparaAnalysis, \
    GenomeDatabase, GenomeEvent, GenomeFeature, GenomeVariation, \
    ComparaAnalysis, ComparaAnalysisEvent


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'


class GenomeDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeDatabase
        exclude = ['genome_database_id', 'genome', 'species_id']


class GenomeSerializer(serializers.ModelSerializer):
    assembly = AssemblySerializer(many=False, required=False)
    organism = OrganismSerializer(many=False, required=False)
    databases = GenomeDatabaseSerializer(many=True, required=False)

    class Meta:
        model = Genome
        exclude = ['genome_id', 'created']


class GenomeAlignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeAlignment
        fields = '__all__'


class GenomeAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeAnnotation
        fields = ['type', 'value']


class GenomeComparaAnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenomeComparaAnalysis
        fields = ('genome', 'compara_analysis')


class GenomeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeEvent
        fields = '__all__'


class GenomeFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeFeature
        fields = '__all__'


class GenomeVariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeVariation
        fields = ('type', 'name', 'count')


class ComparaAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparaAnalysis
        fields = '__all__'


class ComparaAnalysisEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparaAnalysisEvent
        fields = '__all__'
