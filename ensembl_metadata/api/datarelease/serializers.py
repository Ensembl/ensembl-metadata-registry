from rest_framework import serializers
from ensembl_metadata.models.datarelease import DataRelease, EnsemblSite


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnsemblSite
        exclude = ['site_id']


class DataReleaseSerializer(serializers.ModelSerializer):
    site = SiteSerializer(many=False, required=True)

    class Meta:
        model = DataRelease
        exclude = ['data_release_id', 'label']
