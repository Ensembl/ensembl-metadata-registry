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
from datarelease.models import DataRelease
from datarelease.utils import DataReleaseUtils


class DataReleaseUtilsTest(APITestCase):
    fixtures = ['data_release']
    multi_db = True

    def test_loaddata(self):
        datarelease = DataRelease.objects.get(pk=1)
        self.assertEqual(1, datarelease.data_release_id)
        self.assertEqual(80, datarelease.ensembl_version)

        all_ = DataRelease.objects.all()
        self.assertEquals(len(all_), 5)

    def test_get_latest_ensembl_version(self):
        ensembl_version = DataReleaseUtils.get_latest_ensembl_version()
        self.assertEqual(83, ensembl_version, 'Got the right ensembl version')

    def test_get_latest_ensemblgenomes_version(self):
        ensemblgenomes_version = DataReleaseUtils.get_latest_ensemblgenomes_version()
        self.assertEqual(27, ensemblgenomes_version, 'Got the right ensemblgenomes_version version')
