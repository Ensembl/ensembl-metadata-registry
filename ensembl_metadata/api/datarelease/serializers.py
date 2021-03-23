from rest_framework import serializers
from ensembl_metadata.models.datarelease import DataRelease, Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        exclude = ['site_id']


class DataReleaseSerializer(serializers.ModelSerializer):
    site = SiteSerializer(many=False, required=True)

    class Meta:
        model = DataRelease
        exclude = ['data_release_id', 'label']
