from ensembl_metadata.models.datarelease import DataRelease


class DataReleaseUtils(object):

    @classmethod
    def get_latest_version(cls):
        # TODO: evaluate whether this function remains useful.
        # If so, require a site constraint, in order to return a single value;
        # and make exception handling more specific.
        datarelease = None
        try:
            datarelease = DataRelease.objects.filter(is_current=1)[0]
        except:
            return None

        if datarelease is not None:
            return datarelease.version
        return None
