from ensembl_metadata.models.genome import Division


class DivisionUtils(object):

    @classmethod
    def get_all_division_names(cls, eg_only=False):
        division = Division.objects.all()

        if division is not None:
            if eg_only is True:
                all_divisions = list(division.values_list('name', flat=True))
                eg_only_divisions = [div for div in all_divisions if div.lower() not in ['ensembl', 'ensemblgenomes']]
                return eg_only_divisions
            else:
                return list(division.values_list('name', flat=True))

        return None

    @classmethod
    def get_all_division_short_names(cls, eg_only=False):
        division = Division.objects.all()

        if division is not None:
            if eg_only is True:
                pass
            else:
                return list(division.values_list('short_name', flat=True))

        return None
