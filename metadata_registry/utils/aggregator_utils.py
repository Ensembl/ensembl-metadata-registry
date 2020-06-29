"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from django.db.models import Q
from django.db.models.aggregates import Count

from metadata_registry.models.genomeinfo import Genome
from metadata_registry.utils.division import DivisionUtils


class AggregatorUtils(object):

    @classmethod
    def get_db_count(self, division='ensemblvertebrates'):

        queryset = None
        division = division.lower()
        if division == 'ensemblvertebrates':
            queryset = Genome.objects.filter(
                division__name='EnsemblVertebrates').\
                values('division__name', 'data_release__ensembl_version').\
                annotate(Count("genome_id"))
        elif 'genomes' in division:
            queryset = Genome.objects.filter(
                ~Q(division__name='Ensembl')).\
                values('division__name','data_release__ensembl_genomes_version').\
                annotate(Count("genome_id"))
        elif division in [d.lower() for d in DivisionUtils.get_all_division_names(eg_only=True)]:
            queryset = Genome.objects.filter(
                division__name=division).\
                values('division__name', 'data_release__ensembl_genomes_version').\
                annotate(Count("genome_id"))
        else:
            return queryset
        return queryset.order_by('-data_release__ensembl_version', 'division__name')
