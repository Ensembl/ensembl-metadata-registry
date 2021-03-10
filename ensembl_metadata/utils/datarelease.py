from ensembl_metadata.models.datarelease import DataRelease


class DataReleaseUtils(object):

    @classmethod
    def get_latest_version(cls):
        datarelease = None
        try:
            datarelease = DataRelease.objects.filter(is_current=1)[0]
        except:
            return None

        if datarelease is not None:
            return datarelease.version
        return None
