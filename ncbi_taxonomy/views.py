from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from ncbi_taxonomy.models import TaxonomyName, TaxonomyNode
from ncbi_taxonomy.api.serializers import TaxonomyNameSerializer, TaxonomyNodeSerializer
from ncbi_taxonomy.api.filters import TaxonomyFilterBackend


class TaxonomyNodeList(generics.ListAPIView):
    """
    Return a list of taxon records.
    """
    name = 'Taxonomy List'

    queryset = TaxonomyNode.objects.all()
    serializer_class = TaxonomyNodeSerializer
    filter_backends = [TaxonomyFilterBackend]


class TaxonomyNodeDetail(generics.RetrieveAPIView):
    """
    Return a single taxon record.
    """
    name = 'Taxonomy Detail'

    queryset = TaxonomyNode.objects.all()
    serializer_class = TaxonomyNodeSerializer
    lookup_field = 'taxon_id'


class TaxonomyNameList(generics.ListAPIView):
    """
    Return a list of taxon names.
    """
    name = 'Taxonomy Names'

    queryset = TaxonomyName.objects.all()
    serializer_class = TaxonomyNameSerializer
    filter_backends = [DjangoFilterBackend, TaxonomyFilterBackend]
    filterset_fields = ['name_class']
