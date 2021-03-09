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
from metadata_registry.models.organism import Organism, OrganismAlias, OrganismPublication
from metadata_registry.api.organism.serializers import OrganismSerializer, OrganismAliasSerializer,\
    OrganismPublicationSerializer
from metadata_registry.api.organism.filters import OrganismFilterBackend, \
    OrganismAliasOrganismFilterBackend,\
    OrganismPublicationOrganismFilterBackend, OrganismExpandFilterBackend,\
    OganismTaxonomyFilterBackend, OrganismOrganismAliasFilterBackend
from metadata_registry.utils.decorators import setup_eager_loading
from rest_framework.pagination import PageNumberPagination
from metadata_registry.views.base import DataTableListApi
from metadata_registry.utils.schema_utils import SchemaUtils


class OrganismList(generics.ListAPIView):
    queryset = Organism.objects.all()
    serializer_class = OrganismSerializer
    filter_backends = (OrganismExpandFilterBackend, OrganismFilterBackend,
                       OrganismOrganismAliasFilterBackend, OganismTaxonomyFilterBackend,
                       )

    @setup_eager_loading(OrganismSerializer)
    def get_queryset(self):
        queryset = Organism.objects.order_by('pk')
        return queryset


class OrganismDatatableView(DataTableListApi):
    serializer_class = OrganismSerializer
    search_parameters = SchemaUtils.get_field_names(app_name='metadata_registry', model_name='organism', exclude_pk=False)
    default_order_by = 5
    queryset = Organism.objects.all()


class OrganismDetail(generics.RetrieveAPIView):
    queryset = Organism.objects.all()
    serializer_class = OrganismSerializer


class OrganismAliasList(generics.ListAPIView):
    queryset = OrganismAlias.objects.order_by('pk')
    serializer_class = OrganismAliasSerializer
    filter_backends = (OrganismAliasOrganismFilterBackend,)


class OrganismAliasDetail(generics.RetrieveAPIView):
    queryset = OrganismAlias.objects.all()
    serializer_class = OrganismAliasSerializer


class OrganismPublicationList(generics.ListAPIView):
    queryset = OrganismPublication.objects.all()
    serializer_class = OrganismPublicationSerializer
    filter_backends = (OrganismPublicationOrganismFilterBackend,)


class OrganismPublicationDetail(generics.RetrieveAPIView):
    queryset = OrganismPublication.objects.all()
    serializer_class = OrganismPublicationSerializer


# ============For Datatables========
class NotPaginatedSetPagination(PageNumberPagination):
    page_size = None


class OrganismInfoView(generics.ListAPIView):
    serializer_class = OrganismSerializer
    pagination_class = NotPaginatedSetPagination

    @setup_eager_loading(OrganismSerializer)
    def get_queryset(self):
        queryset = Organism.objects.order_by('pk')
        return queryset
