'''
Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2017] EMBL-European Bioinformatics Institute

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


from __future__ import unicode_literals
from rest_framework import generics
from genomeinfo.models import Genome, GenomeAlignment, GenomeAnnotation, GenomeComparaAnalysis, \
                              GenomeDatabase, GenomeEvent, GenomeFeature, GenomeVariation
from genomeinfo.drf.serializers import GenomeSerializer, GenomeAlignmentSerializer, \
                                       GenomeAnnotationSerializer, GenomeComparaAnalysisSerializer, \
                                       GenomeDatabaseSerializer, GenomeEventSerializer, GenomeFeatureSerializer, \
                                       GenomeVariationSerializer
from genomeinfo.drf.filters import GenomeFilterBackend, GenomeComparaFilterBackend, GenomeVariationFilterBackend,\
    GenomeDatareleaseFilterBackend, GenomeAssemblyFilterBackend,\
    GenomeDatabasereleaseFilterBackend, GenomeExpandFilterBackend,\
    GenomeDivisionFilterBackend
from organism.drf.filters import OrganismAliasOrganismFilterBackend
from ensembl_metadata_registry.utils.decorators import setup_eager_loading
from rest_framework.pagination import PageNumberPagination


class GenomeList(generics.ListAPIView):

    serializer_class = GenomeSerializer
    filter_backends = (GenomeExpandFilterBackend, GenomeFilterBackend, GenomeDatabasereleaseFilterBackend,
                       GenomeComparaFilterBackend, GenomeVariationFilterBackend, GenomeDatareleaseFilterBackend,
                       GenomeAssemblyFilterBackend, OrganismAliasOrganismFilterBackend, GenomeDivisionFilterBackend)

    @setup_eager_loading(GenomeSerializer)
    def get_queryset(self):
        queryset = Genome.objects.order_by('pk')
        return queryset


class GenomeDetail(generics.RetrieveAPIView):
    queryset = Genome.objects.all()
    serializer_class = GenomeSerializer


class GenomeAlignmentList(generics.ListAPIView):
    queryset = GenomeAlignment.objects.order_by('pk')
    serializer_class = GenomeAlignmentSerializer


class GenomeAlignmentDetail(generics.RetrieveAPIView):
    queryset = GenomeAlignment.objects.all()
    serializer_class = GenomeAlignmentSerializer


class GenomeAnnotationList(generics.ListAPIView):
    queryset = GenomeAnnotation.objects.order_by('pk')
    serializer_class = GenomeAnnotationSerializer


class GenomeAnnotationDetail(generics.RetrieveAPIView):
    queryset = GenomeAnnotation.objects.all()
    serializer_class = GenomeAnnotationSerializer


class GenomeComparaAnalysisList(generics.ListAPIView):
    queryset = GenomeComparaAnalysis.objects.order_by('pk')
    serializer_class = GenomeComparaAnalysisSerializer


class GenomeComparaAnalysisDetail(generics.RetrieveAPIView):
    queryset = GenomeComparaAnalysis.objects.all()
    serializer_class = GenomeComparaAnalysisSerializer


class GenomeDatabaseList(generics.ListAPIView):
    queryset = GenomeDatabase.objects.order_by('pk')
    serializer_class = GenomeDatabaseSerializer


class GenomeDatabaseDetail(generics.RetrieveAPIView):
    queryset = GenomeDatabase.objects.all()
    serializer_class = GenomeDatabaseSerializer


class GenomeEventList(generics.ListAPIView):
    queryset = GenomeEvent.objects.order_by('pk')
    serializer_class = GenomeEventSerializer


class GenomeEventDetail(generics.RetrieveAPIView):
    queryset = GenomeEvent.objects.all()
    serializer_class = GenomeEventSerializer


class GenomeFeatureList(generics.ListAPIView):
    queryset = GenomeFeature.objects.all()
    serializer_class = GenomeFeatureSerializer


class GenomeFeatureDetail(generics.RetrieveAPIView):
    queryset = GenomeFeature.objects.order_by('pk')
    serializer_class = GenomeFeatureSerializer


class GenomeVariationList(generics.ListAPIView):
    queryset = GenomeVariation.objects.order_by('pk')
    serializer_class = GenomeVariationSerializer


class GenomeVariationDetail(generics.RetrieveAPIView):
    queryset = GenomeVariation.objects.all()
    serializer_class = GenomeVariationSerializer


# class NoPaginatedSetPagination(PageNumberPagination):
#     page_size = None


class NotPaginatedSetPagination(PageNumberPagination):
    page_size = None


class GenomeInfoView(generics.ListAPIView):
    serializer_class = GenomeSerializer
    pagination_class = NotPaginatedSetPagination
    filter_backends = (GenomeExpandFilterBackend, GenomeFilterBackend, GenomeDatabasereleaseFilterBackend,
                       GenomeComparaFilterBackend, GenomeVariationFilterBackend, GenomeDatareleaseFilterBackend,
                       GenomeAssemblyFilterBackend, OrganismAliasOrganismFilterBackend, GenomeDivisionFilterBackend)

    @setup_eager_loading(GenomeSerializer)
    def get_queryset(self):
        queryset = Genome.objects.order_by('pk')
        return queryset
