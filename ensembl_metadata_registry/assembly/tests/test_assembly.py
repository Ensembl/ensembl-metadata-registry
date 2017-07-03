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

from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from assembly.models import Assembly
import json


class AssemblyTest(APITestCase):
    fixtures = ['assembly']
    multi_db = True

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
        self.assertEqual(json_response['count'], 5)
        self.assertEqual(json_response['results'][0], {'assembly_ucsc': None, 'base_count': 177003750,
                                                       'assembly_accession': None,
                                                       'assembly_level': 'reftig', 'assembly_id': 1,
                                                       'assembly_name': 'CSAV 2.0'})

        response = client.get('/assembly/1/')
        self.assertEqual(response.status_code, 200)
        json_response = (json.loads(response.content.decode('utf8')))
        self.assertEqual(json_response, {'assembly_ucsc': None, 'base_count': 177003750, 'assembly_accession': None,
                                         'assembly_level': 'reftig', 'assembly_id': 1, 'assembly_name': 'CSAV 2.0'})
