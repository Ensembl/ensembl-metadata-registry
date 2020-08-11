"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""



from rest_framework import generics
from metadata_registry_current.models.datarelease import DataRelease
from metadata_registry_current.api.datarelease.serializers import DataReleaseSerializer
from metadata_registry_current.api.datarelease.filters import DatareleaseFilterBackend
from rest_framework.pagination import PageNumberPagination
from metadata_registry_current.utils.decorators import setup_eager_loading
from metadata_registry_current.views.base import DataTableListApi
from metadata_registry_current.utils.schema_utils import SchemaUtils


class DataReleaseList(generics.ListAPIView):
    queryset = DataRelease.objects.all()
    serializer_class = DataReleaseSerializer
    filter_backends = (DatareleaseFilterBackend,)


class DataReleaseDatatableViewCurrent(DataTableListApi):
    serializer_class = DataReleaseSerializer
    search_parameters = SchemaUtils.get_field_names(app_name='metadata_registry_current', model_name='datarelease', exclude_pk=False)
    default_order_by = 2
    queryset = DataRelease.objects.all()


class DataReleaseDetail(generics.RetrieveAPIView):
    queryset = DataRelease.objects.all()
    serializer_class = DataReleaseSerializer

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
