'''
Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2019] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from genomeinfo.models import Genome, GenomeAlignment, GenomeAnnotation, GenomeComparaAnalysis, \
                              GenomeDatabase, GenomeEvent, GenomeFeature, GenomeVariation
from rest_framework import serializers
from compara.drf.serializers import ComparaAnalysisSerializer
from organism.drf.serializers import OrganismSerializer
from datarelease.drf.serializers import DataReleaseSerializer
from assembly.drf.serializers import AssemblySerializer
from division.drf.serializers import DivisionSerializer
from ensembl_metadata_registry.utils.drf_mixin import SerializerMixin


class GenomeAlignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeAlignment
        fields = '__all__'


class GenomeAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeAnnotation
        fields = '__all__'


class GenomeDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenomeDatabase
        fields = '__all__'


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


class GenomeSerializer(SerializerMixin, serializers.ModelSerializer,):

    """
    A ModelSerializer that controls which fields should be displayed.
    """
    MANY2ONE_SERIALIZER = {Genome.MANY2ONE_RELATED['DATA_RELEASE']: DataReleaseSerializer,
                           Genome.MANY2ONE_RELATED['ASSEMBLY']: AssemblySerializer,
                           Genome.MANY2ONE_RELATED['ORGANISM']: OrganismSerializer,
                           Genome.MANY2ONE_RELATED['DIVISION']: DivisionSerializer}

    ONE2MANY_SERIALIZER = {Genome.ONE2MANY_RELATED['GENOME_ALIGNMENT']: GenomeAlignmentSerializer,
                           Genome.ONE2MANY_RELATED['GENOME_ANNOTATION']: GenomeAnnotationSerializer,
                           Genome.ONE2MANY_RELATED['GENOME_DATABASE']: GenomeDatabaseSerializer,
                           Genome.ONE2MANY_RELATED['GENOME_EVENT']: GenomeEventSerializer,
                           Genome.ONE2MANY_RELATED['GENOME_FEATURE']: GenomeFeatureSerializer,
                           Genome.ONE2MANY_RELATED['GENOME_VARIATION']: GenomeVariationSerializer,
                           Genome.ONE2MANY_RELATED['GENOME_COMPARA_ANALYSIS']: ComparaAnalysisSerializer
                           }

    class Meta:
        model = Genome
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GenomeSerializer, self).__init__(*args, **kwargs)
        self.set_related_fields(GenomeSerializer, **kwargs)


class GenomeComparaAnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = GenomeComparaAnalysis
        fields = ('genome', 'compara_analysis')
