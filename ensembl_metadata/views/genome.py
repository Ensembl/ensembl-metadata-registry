from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from ensembl_metadata.models.assembly import Assembly
from ensembl_metadata.models.genome import Genome, GenomeDatabase, GenomeAnnotation
from ensembl_metadata.models.organism import Organism
from ensembl_metadata.api.genome.serializers import \
    GenomeSerializer, GenomeDatabaseSerializer, GenomeAnnotationSerializer


class GenomeList(generics.ListAPIView):
    """
    Return a list of genomes.
    """
    name = 'Genomes'

    queryset = Genome.objects.all()
    serializer_class = GenomeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['organism__name', 'organism__scientific_name', 'organism__taxonomy_id']
    ordering_fields = ['organism__name', 'organism__scientific_name', 'organism__taxonomy_id']
    ordering = ['organism__name']


class GenomeDetail(generics.RetrieveAPIView):
    """
    Return a single genome.
    """
    name = 'Genome'

    queryset = Genome.objects.all()
    serializer_class = GenomeSerializer
    lookup_field = 'genome_uuid'
    lookup_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['databases'] = GenomeDatabase.objects.all()
        return context


class GenomeAnnotationList(generics.ListAPIView):
    """
    Return a list of annotations on a genome.
    """
    name = 'Annotations'

    queryset = GenomeAnnotation.objects.all()
    serializer_class = GenomeAnnotationSerializer

    def get_queryset(self):
        return GenomeAnnotation.objects.filter(
            genome__genome_uuid=self.kwargs['uuid'])
