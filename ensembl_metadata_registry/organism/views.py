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
from organism.models import Organism, OrganismAlias, OrganismPublication
from organism.drf.serializers import OrganismSerializer, OrganismAliasSerializer,\
    OrganismPublicationSerializer
from organism.drf.filters import OrganismFilterBackend, \
    OrganismAliasOrganismFilterBackend,\
    OrganismPublicationOrganismFilterBackend, OrganismExpandFilterBackend,\
    OganismTaxonomyFilterBackend, OrganismOrganismAliasFilterBackend
from ensembl_metadata_registry.utils.decorators import setup_eager_loading


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


class OrganismDetail(generics.RetrieveAPIView):
    queryset = Organism.objects.all()
    serializer_class = OrganismSerializer


class OrganismAliasList(generics.ListAPIView):
    queryset = OrganismAlias.objects.all()
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
