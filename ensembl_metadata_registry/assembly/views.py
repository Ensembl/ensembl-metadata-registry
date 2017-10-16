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
from assembly.models import Assembly, AssemblySequence
from assembly.drf.serializers import AssemblySerializer, AssemblySequenceSerializer
from rest_framework import generics
from assembly.drf.filters import AssemblyFilterBackend, AssemblySequenceFilterBackend,\
    AssemblyExpandFilterBackend
from ensembl_metadata_registry.utils.decorators import setup_eager_loading
from ensembl_metadata_registry.views import DataTableListApi
from ensembl_metadata_registry.utils.schema_utils import SchemaUtils


class AssemblyList(generics.ListAPIView):
    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer
    filter_backends = (AssemblyExpandFilterBackend, AssemblyFilterBackend,)

    @setup_eager_loading(AssemblySerializer)
    def get_queryset(self):
        queryset = Assembly.objects.order_by('pk')
        return queryset


class AssemblyDatatableView(DataTableListApi):
    serializer_class = AssemblySerializer
    search_parameters = SchemaUtils.get_field_names(app_name='assembly', model_name='assembly', exclude_pk=False)
    default_order_by = 3
    queryset = Assembly.objects.all()


class AssemblyDetail(generics.RetrieveAPIView):
    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer


class AssemblySequenceList(generics.ListAPIView):
    queryset = AssemblySequence.objects.all()
    serializer_class = AssemblySequenceSerializer
    filter_backends = (AssemblySequenceFilterBackend,)


class AssemblySequenceDetail(generics.RetrieveAPIView):
    queryset = AssemblySequence.objects.all()
    serializer_class = AssemblySequenceSerializer
