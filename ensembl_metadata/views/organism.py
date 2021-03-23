from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from ensembl_metadata.models.organism import Organism
from ensembl_metadata.api.organism.serializers import OrganismSerializer


class OrganismList(generics.ListAPIView):
    """
    Return a list of organisms.
    """
    name = 'Organisms'

    queryset = Organism.objects.all()
    serializer_class = OrganismSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name', 'scientific_name', 'taxonomy_id']
    ordering_fields = ['name', 'scientific_name', 'taxonomy_id']
    ordering = ['name']


class OrganismDetail(generics.RetrieveAPIView):
    """
    Return a single organism.
    """
    name = 'Organism'

    queryset = Organism.objects.all()
    serializer_class = OrganismSerializer
    lookup_field = 'name'
