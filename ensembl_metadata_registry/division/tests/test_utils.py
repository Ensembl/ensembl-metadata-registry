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


from rest_framework.test import APITestCase
from division.models import Division
from division.utils import DivisionUtils


class DivisionUtilsTest(APITestCase):
    fixtures = ['division']
    multi_db = True

    def test_loaddata(self):
        division = Division.objects.get(pk=1)
        self.assertEqual('Ensembl', division.name)

    def test_get_all_division_names(self):
        division_names = DivisionUtils.get_all_division_names()
        self.assertIn('Ensembl', division_names, 'Ensembl in division names')

    def test_get_all_division_short_names(self):
        division_short_names = DivisionUtils.get_all_division_short_names()
        self.assertIn('EM', division_short_names, 'EM in division short names')
