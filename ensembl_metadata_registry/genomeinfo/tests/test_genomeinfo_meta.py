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
from genomeinfo.models import Genome
from ensembl_metadata_registry.utils.drf_utils import DrfUtils


class GenomeinfoMetaTest(APITestCase):
    """Tests to check _meta info"""

    def test_get_related_entities(self):
        one2many = DrfUtils.get_related_entities(Genome, 'one2many')
        print(one2many)

        many2one = DrfUtils.get_related_entities(Genome, 'many2one')
        print(many2one)

        many2many = DrfUtils.get_related_entities(Genome, 'many2many')
        print(many2many)

        many2one = DrfUtils.get_related_entities(Genome)
        print(many2one)
