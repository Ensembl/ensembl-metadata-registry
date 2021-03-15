from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from ensembl_metadata.models.genome import Genome, Dataset
from ensembl_metadata.api.genome.serializers import GenomeSerializer


class GenomeList(generics.ListAPIView):
    """
    Return a list of genomes.
    """
    name = 'Genomes'

    queryset = Genome.objects.all()
    serializer_class = GenomeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['ensembl_name', 'scientific_name', 'taxonomy_id']
    ordering_fields = ['ensembl_name', 'scientific_name', 'taxonomy_id']
    ordering = ['scientific_name']


class GenomeDetail(generics.RetrieveAPIView):
    """
    Return a single genome.
    """
    name = 'Genome'

    queryset = Genome.objects.all()
    serializer_class = GenomeSerializer
    lookup_field = 'genome_uuid'
