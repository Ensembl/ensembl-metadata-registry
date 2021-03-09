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
from metadata_registry.models.division import Division
from metadata_registry.api.division.serializers import DivisionSerializer
from metadata_registry.api.division.filters import DivisionFilterBackend
from rest_framework.pagination import PageNumberPagination
from metadata_registry.utils.decorators import setup_eager_loading
from metadata_registry.views.base import DataTableListApi
from metadata_registry.utils.schema_utils import SchemaUtils


class DivisionList(generics.ListAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    filter_backends = (DivisionFilterBackend,)


class DivisionDetail(generics.RetrieveAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer


class DivisionDatatableView(DataTableListApi):
    serializer_class = DivisionSerializer
    search_parameters = SchemaUtils.get_field_names(app_name='metadata_registry', model_name='division', exclude_pk=False)
    default_order_by = 2
    queryset = Division.objects.all()


# ============For Datatables========
class NotPaginatedSetPagination(PageNumberPagination):
    page_size = None


class DivisionInfoView(generics.ListAPIView):
    serializer_class = DivisionSerializer
    pagination_class = NotPaginatedSetPagination

    @setup_eager_loading(DivisionSerializer)
    def get_queryset(self):
        queryset = Division.objects.order_by('pk')
        return queryset
