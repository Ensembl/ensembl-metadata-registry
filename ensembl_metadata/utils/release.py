from ensembl_metadata.models.release import Release


class ReleaseUtils(object):

    @classmethod
    def get_latest_version(cls):
        release = None
        try:
            release = Release.objects.filter(is_current=1)[0]
        except:
            return None

        if release is not None:
            return release.version
        return None
