from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from ensembl_metadata.models.datarelease import DataRelease
from ensembl_metadata.api.datarelease.serializers import DataReleaseSerializer


class DataReleaseList(generics.ListAPIView):
    """
    Return a list of releases.
    """
    name = 'Releases'

    queryset = DataRelease.objects.all()
    serializer_class = DataReleaseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_current']
    ordering_fields = ['version', 'release_date']
    ordering = ['version']

    def get_queryset(self):
        version = self.kwargs.get('version', None)
        if version is not None:
            queryset = DataRelease.objects.filter(version=version)
        else:
            queryset = DataRelease.objects.all()
        return queryset


class DataReleaseDetail(generics.RetrieveAPIView):
    """
    Return a single release.
    """
    name = 'Release'

    queryset = DataRelease.objects.all()
    serializer_class = DataReleaseSerializer

    def get_object(self):
        version = self.kwargs['version']
        site_label = self.kwargs['site']
        obj = DataRelease.objects.get(version=version, site__label__startswith=site_label)
        return obj
