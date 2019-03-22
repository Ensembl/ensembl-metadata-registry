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


from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from genomeinfo.models import Genome


class GenomeinfoTest(APITestCase):
    fixtures = ['genomeinfo_division', 'genomeinfo_genome', 'genomeinfo_genome_alignment',
                'genomeinfo_genome_annotation',
                'genomeinfo_genome_compara_analysis', 'genomeinfo_genome_databases', 'genomeinfo_genome_event',
                'genomeinfo_genome_feature', 'genomeinfo_genome_variation']
    multi_db = True

    def test_loaddata(self):
        genome = Genome.objects.get(pk=1)
        self.assertEqual(1, genome.assembly_id)
        self.assertEqual(1, genome.division_id)

    def test_api_request(self):
        # Using the standard APIClient to create a GET request
        client = APIClient()
        response = client.get('/genome/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/genome/1/')
        self.assertEqual(response.status_code, 200)
