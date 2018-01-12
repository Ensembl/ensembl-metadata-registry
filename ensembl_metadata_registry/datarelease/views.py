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
from datarelease.models import DataRelease, DataReleaseDatabase, DataReleaseDatabaseEvent
from datarelease.drf.serializers import DataReleaseSerializer, \
    DataReleaseDatabaseSerializer, DataReleaseDatabaseEventSerializer
from datarelease.drf.filters import DatareleaseFilterBackend
from rest_framework.pagination import PageNumberPagination
from ensembl_metadata_registry.utils.decorators import setup_eager_loading
from ensembl_metadata_registry.views import DataTableListApi
from ensembl_metadata_registry.utils.schema_utils import SchemaUtils


class DataReleaseList(generics.ListAPIView):
    queryset = DataRelease.objects.all()
    serializer_class = DataReleaseSerializer
    filter_backends = (DatareleaseFilterBackend,)


class DataReleaseDatatableView(DataTableListApi):
    serializer_class = DataReleaseSerializer
    search_parameters = SchemaUtils.get_field_names(app_name='datarelease', model_name='datarelease', exclude_pk=False)
    default_order_by = 2
    queryset = DataRelease.objects.all()


class DataReleaseDetail(generics.RetrieveAPIView):
    queryset = DataRelease.objects.all()
    serializer_class = DataReleaseSerializer


class DataReleaseDatabaseList(generics.ListAPIView):
    queryset = DataReleaseDatabase.objects.all()
    serializer_class = DataReleaseDatabaseSerializer


class DataReleaseDatabaseDetail(generics.RetrieveAPIView):
    queryset = DataReleaseDatabase.objects.all()
    serializer_class = DataReleaseDatabaseSerializer


class DataReleaseDatabaseEventList(generics.ListAPIView):
    queryset = DataReleaseDatabaseEvent.objects.all()
    serializer_class = DataReleaseDatabaseEventSerializer


class DataReleaseDatabaseEventDetail(generics.RetrieveAPIView):
    queryset = DataReleaseDatabaseEvent.objects.all()
    serializer_class = DataReleaseDatabaseEventSerializer


# ============For Datatables========
class NotPaginatedSetPagination(PageNumberPagination):
    page_size = None


class DatareleaseInfoView(generics.ListAPIView):
    serializer_class = DataReleaseSerializer
    pagination_class = NotPaginatedSetPagination

    @setup_eager_loading(DataReleaseSerializer)
    def get_queryset(self):
        queryset = DataRelease.objects.order_by('pk')
        return queryset
