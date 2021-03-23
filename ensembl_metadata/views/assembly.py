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
    search_fields = ['^assembly_accession', '^assembly_name', '^assembly_ucsc']
    ordering_fields = ['assembly_accession']
    ordering = ['assembly_accession']


class AssemblyDetail(generics.RetrieveAPIView):
    """
    Return a single assembly.
    """
    name = 'Assembly'

    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer
    lookup_field = 'assembly_accession'
    lookup_url_kwarg = 'accession'


class AssemblySequenceList(generics.ListAPIView):
    """
    Return a list of sequences.
    """
    name = 'Sequences'

    queryset = AssemblySequence.objects.all()
    serializer_class = AssemblySequenceSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['chromosomal']
    ordering_fields = ['acc', 'name']
    ordering = ['acc']

    def get_queryset(self):
        return AssemblySequence.objects.filter(
            assembly__assembly_accession=self.kwargs['accession'])
