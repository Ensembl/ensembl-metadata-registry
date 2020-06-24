'''
Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2019] EMBL-European Bioinformatics Institute

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


from rest_framework.test import APITestCase
from metadata_registry.models.genomeinfo import Genome
from metadata_registry.utils.aggregator_utils import AggregatorUtils


class AggregatorUtilsTest(APITestCase):
    fixtures = ['genomeinfo_division', 'genomeinfo_genome', 'genomeinfo_genome_alignment',
                'genomeinfo_genome_annotation', 'genomeinfo_genome_compara_analysis',
                'genomeinfo_genome_databases',
                'genomeinfo_genome_feature', 'genomeinfo_genome_variation']
    multi_db = True

    def test_loaddata(self):
        genome = Genome.objects.get(pk=1)
        self.assertEqual(1, genome.assembly_id)
        self.assertEqual(1, genome.division_id)

    def test_get_db_count(self):

        queryset = AggregatorUtils.get_db_count(division="ensemblvertebrates")
        expected_queryset = [{'data_release__ensembl_version': 80, 'division__name': 'EnsemblVertebrates',
                              'genome_id__count': 9},
                             {'data_release__ensembl_version': 81, 'division__name': 'EnsemblVertebrates',
                              'genome_id__count': 5}]

        self.assertListEqual(expected_queryset, list(queryset), "Results are equal for EnsemblVertebrates")

        queryset_eg = AggregatorUtils.get_db_count(division="ensembl_genomes")
        expected_queryset_eg = [{'data_release__ensembl_genomes_version': None, 'genome_id__count': 9,
                                 'division__name': 'EnsemblVertebrates'},
                                {'data_release__ensembl_genomes_version': 27,
                                 'genome_id__count': 5, 'division__name': 'EnsemblVertebrates'},
                                {'data_release__ensembl_genomes_version': 27, 'genome_id__count': 1,
                                 'division__name': 'EnsemblProtists'}]
        self.assertListEqual(expected_queryset_eg, list(queryset_eg), "Results are equal for eg")
