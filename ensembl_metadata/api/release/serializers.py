from rest_framework import serializers
from ensembl_metadata.models.release import Release, Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        exclude = ['site_id']


class ReleaseSerializer(serializers.ModelSerializer):
    site = SiteSerializer(many=False, required=True)

    class Meta:
        model = Release
        exclude = ['release_id']
