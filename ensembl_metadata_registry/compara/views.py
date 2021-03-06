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

from __future__ import unicode_literals
from rest_framework import generics
from compara.models import ComparaAnalysis, ComparaAnalysisEvent
from compara.drf.serializers import ComparaAnalysisSerializer,\
    ComparaAnalysisEventSerializer
from compara.drf.filters import ComparaExpandFilterBackend
from ensembl_metadata_registry.utils.decorators import setup_eager_loading


class ComparaAnalysisList(generics.ListAPIView):
    queryset = ComparaAnalysis.objects.all()
    serializer_class = ComparaAnalysisSerializer
    filter_backends = (ComparaExpandFilterBackend, )

    @setup_eager_loading(ComparaAnalysisSerializer)
    def get_queryset(self):
        queryset = ComparaAnalysis.objects.order_by('pk')
        return queryset


class ComparaAnalysisDetail(generics.RetrieveAPIView):
    queryset = ComparaAnalysis.objects.all()
    serializer_class = ComparaAnalysisSerializer


class ComparaAnalysisEventList(generics.ListAPIView):
    queryset = ComparaAnalysisEvent.objects.all()
    serializer_class = ComparaAnalysisEventSerializer


class ComparaAnalysisEventDetail(generics.RetrieveAPIView):
    queryset = ComparaAnalysisEvent.objects.all()
    serializer_class = ComparaAnalysisEventSerializer
