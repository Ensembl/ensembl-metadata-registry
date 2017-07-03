'''
Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2017] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from genomeinfo.models import Genome
from django.db.models.aggregates import Count
from django.db.models import Q
from division.utils import DivisionUtils


class AggregatorUtils(object):

    @classmethod
    def get_db_count(self, division='ensembl'):

        queryset = None
        division = division.lower()
        if division == 'ensembl':
            queryset = Genome.objects.filter(
                 division__name='Ensembl').values('division__name',
                                                  'data_release__' + division + '_version').order_by().annotate(
                                             Count("genome_id"))
        elif 'genomes' in division:
            queryset = Genome.objects.filter(
                 ~Q(division__name='Ensembl')).values('division__name',
                                                      'data_release__ensembl_genomes_version').order_by().annotate(
                                             Count("genome_id"))
        elif division in [d.lower() for d in DivisionUtils.get_all_division_names(eg_only=True)]:
            queryset = Genome.objects.filter(
                 division__name=division).values('division__name',
                                                 'data_release__ensembl_genomes_version').order_by().annotate(
                                             Count("genome_id"))

        return queryset
