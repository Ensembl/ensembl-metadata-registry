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
from ncbi_taxonomy.models import NcbiTaxaName, NcbiTaxaNode
from ncbi_taxonomy.api.serializers import NcbiTaxaNameSerializer, NcbiTaxaNodeSerializer
from metadata_registry.utils.decorators import setup_eager_loading
from ncbi_taxonomy.api.filters import TaxonomyFilterBackend


class NcbiTaxaNameList(generics.ListAPIView):
    queryset = NcbiTaxaName.objects.all()
    serializer_class = NcbiTaxaNameSerializer
    filter_backends = (TaxonomyFilterBackend,)

    @setup_eager_loading(NcbiTaxaNameSerializer)
    def get_queryset(self):
        queryset = NcbiTaxaName.objects.order_by('pk')
        return queryset


class NcbiTaxaNameDetail(generics.RetrieveAPIView):
    queryset = NcbiTaxaName.objects.all()
    serializer_class = NcbiTaxaNameSerializer


class NcbiTaxaNodeList(generics.ListAPIView):
    queryset = NcbiTaxaNode.objects.all()
    serializer_class = NcbiTaxaNodeSerializer
    filter_backends = (TaxonomyFilterBackend,)

    @setup_eager_loading(NcbiTaxaNodeSerializer)
    def get_queryset(self):
        queryset = NcbiTaxaNode.objects.order_by('pk')
        return queryset


class NcbiTaxaNodeDetail(generics.RetrieveAPIView):
    queryset = NcbiTaxaNode.objects.all()
    serializer_class = NcbiTaxaNodeSerializer
