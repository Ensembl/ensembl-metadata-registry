from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from ensembl_metadata.models.genome import Genome, GenomeRelease

"""
class GenomeinfoTest(APITestCase):
    fixtures = ['genomeinfo_division', 'genomeinfo_genome', 'genomeinfo_genome_alignment',
                'genomeinfo_genome_annotation',
                'genomeinfo_genome_compara_analysis', 'genomeinfo_genome_databases',  # 'genomeinfo_genome_event',
                'genomeinfo_genome_feature', 'genomeinfo_genome_variation']
    multi_db = True

    def test_loaddata(self):
        genome = Genome.objects.get(pk=1)
        genomerelease = GenomeRelease.objects.get(pk=1)
        self.assertEqual(1, genome.assembly_id)
        self.assertEqual(1, genomerelease.division_id)

    def test_api_request(self):
        # Using the standard APIClient to create a GET request
        client = APIClient()
        response = client.get('/genome/')
        self.assertEqual(response.status_code, 200)

        response = client.get('/genome/1/')
        self.assertEqual(response.status_code, 200)
"""
