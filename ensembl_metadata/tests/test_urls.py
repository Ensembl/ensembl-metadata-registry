from django.test import TestCase
from django.urls import reverse


"""
class TestBasicUrls(TestCase):
    fixtures = ['assembly', 'genomeinfo_division', 'compara_analysis', 'data_release', #'compara_analysis_event',
                'genomeinfo_genome', 'genomeinfo_genome', 'genomeinfo_genome_alignment',
                'genomeinfo_genome_annotation',
                'genomeinfo_genome_compara_analysis', 'genomeinfo_genome_databases',  # 'genomeinfo_genome_event',
                'genomeinfo_genome_feature', 'genomeinfo_genome_variation']
    divisions = ['EnsemblMetazoa', 'EnsemblVertebrates', 'EnsemblFungi', 'EnsemblProtists', 'EnsemblBacteria',
                 'EnsemblPlants']

    def test_assembly_urls(self):
        response = self.client.get(reverse('assembly_list'))
        self.assertEqual(response.status_code, 200)

    def test_genomeinfo_urls(self):
        for division in self.divisions:
            response = self.client.get(reverse('get_db_count', kwargs={'division': division}))
            self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('get_db_count', kwargs={'division': 'Ensembl'}))
        self.assertEqual(response.status_code, 200)

    def test_compara_urls(self):
        response = self.client.get(reverse('compara_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('compara_analysis_event_list'))
        self.assertEqual(response.status_code, 200)

    def test_datarelease_urls(self):
        response = self.client.get(reverse('datarelease_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('datarelease_info_nopagination_table'))
        self.assertEqual(response.status_code, 200)

    def test_division_urls(self):
        response = self.client.get(reverse('division_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('datarelease_info_nopagination_table'))
        self.assertEqual(response.status_code, 200)

    def test_genome_urls(self):
        response = self.client.get(reverse('genome_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('genome_alignment_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('genome_annotation_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('genome_compara_analysis_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('genome_database_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('genome_event_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('genome_feature_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('genome_variation_list'))
        self.assertEqual(response.status_code, 200)
        for division in self.divisions:
            response = self.client.get(reverse('genomeinfo_table', kwargs={'division': division}))
            self.assertEqual(response.status_code, 200)

    def test_organism_urls(self):
        response = self.client.get(reverse('organism_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('organism_alias_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('organism_publication_list'))
        self.assertEqual(response.status_code, 200)

    def test_datatable_urls(self):
        datatables = ['organism', 'assembly', 'division']
        for table in datatables:
            response = self.client.get(reverse('datatable_view', kwargs={'table_name': table}))
            self.assertEqual(response.status_code, 200)
            # TODO reactivate if needed
            #response = self.client.get(reverse('datatablefetch_clientside', kwargs={'table_name': table}))
            #self.assertEqual(response.status_code, 200)
            response = self.client.get(reverse('datatablefetch_serverside_assembly'))
            self.assertEqual(response.status_code, 200)
            response = self.client.get(reverse('datatablefetch_serverside_genome'))
            self.assertEqual(response.status_code, 200)
            response = self.client.get(reverse('datatablefetch_serverside_division'))
            self.assertEqual(response.status_code, 200)

    def test_misc_urls(self):
        response = self.client.get(reverse('privacy_note_emr'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('doc_view'))
        self.assertEqual(response.status_code, 200)
"""
