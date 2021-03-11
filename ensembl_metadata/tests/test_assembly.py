import json

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from ensembl_metadata.models.assembly import Assembly


"""
class AssemblyTest(APITestCase):
    # TODO test assembly_sequence once enabled again in urls
    fixtures = ['assembly']
    multi_db = True

    def test_baseurls(self):
        response = self.client.get(reverse('assembly_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('assembly_detail', kwargs={'pk': 4}))
        self.assertEqual(response.status_code, 200)

    def test_loaddata(self):
        assembly = Assembly.objects.get(pk=1)
        self.assertEqual(1, assembly.assembly_id)
        self.assertEqual('CSAV 2.0', assembly.assembly_name)
        all_ = Assembly.objects.all()
        self.assertEquals(len(all_), 5)

    def test_api_request(self):
        # Using the standard APIClient to create a GET request
        client = APIClient()
        response = client.get('/assembly/')
        self.assertEqual(response.status_code, 200)
        json_response = (json.loads(response.content.decode('utf8')))

        self.assertEqual(len(json_response['results']), 5)

        expected_assembly_response = {'assembly_name': 'CSAV 2.0',
                                      'assembly_ucsc': None,
                                      'base_count': 177003750, 'assembly_id': 1,
                                      'assembly_default': 'CSAV 2.0',
                                      'assembly_level': 'reftig',
                                      'assembly_accession': None}

        self.assertDictEqual(json_response['results'][0], expected_assembly_response)

        response = client.get('/assembly/1/')
        self.assertEqual(response.status_code, 200)
        json_response = (json.loads(response.content.decode('utf8')))
        self.assertDictEqual(json_response, expected_assembly_response)
"""
