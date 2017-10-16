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

from rest_framework import generics
from division.models import Division
from division.drf.serializers import DivisionSerializer
from division.drf.filters import DivisionFilterBackend
from rest_framework.pagination import PageNumberPagination
from ensembl_metadata_registry.utils.decorators import setup_eager_loading


class DivisionList(generics.ListAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    filter_backends = (DivisionFilterBackend,)


class DivisionDetail(generics.RetrieveAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer


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
