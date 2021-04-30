from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from ensembl_metadata.models.assembly import Assembly, AssemblySequence
from ensembl_metadata.api.assembly.serializers import AssemblySerializer, AssemblySequenceSerializer


class AssemblyList(generics.ListAPIView):
    """
    Return a list of assemblies.
    """
    name = 'Assemblies'

    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['^accession', '^name', '^ucsc_name']
    ordering_fields = ['accession']
    ordering = ['accession']


class AssemblyDetail(generics.RetrieveAPIView):
    """
    Return a single assembly.
    """
    name = 'Assembly'

    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer
    lookup_field = 'accession'


class AssemblySequenceList(generics.ListAPIView):
    """
    Return a list of sequences.
    """
    name = 'Sequences'

    queryset = AssemblySequence.objects.all()
    serializer_class = AssemblySequenceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['chromosomal']
    ordering_fields = ['accession', 'name']
    ordering = ['accession']

    def get_queryset(self):
        return AssemblySequence.objects.filter(
            assembly__accession=self.kwargs['accession'])
