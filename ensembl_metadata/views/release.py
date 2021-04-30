from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from ensembl_metadata.models.release import Release
from ensembl_metadata.api.release.serializers import ReleaseSerializer


class ReleaseList(generics.ListAPIView):
    """
    Return a list of releases.
    """
    name = 'Releases'

    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_current']
    ordering_fields = ['version', 'release_date']
    ordering = ['version']

    def get_queryset(self):
        version = self.kwargs.get('version', None)
        if version is not None:
            queryset = Release.objects.filter(version=version)
        else:
            queryset = Release.objects.all()
        return queryset


class ReleaseDetail(generics.RetrieveAPIView):
    """
    Return a single release.
    """
    name = 'Release'

    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

    def get_object(self):
        version = self.kwargs['version']
        site_name = self.kwargs['site']
        obj = Release.objects.get(version=version, site__name__startswith=site_name)
        return obj
