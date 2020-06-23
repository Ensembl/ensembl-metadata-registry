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
from ncbi_taxonomy.models import NcbiTaxaNode
from ncbi_taxonomy.utils import NcbiTaxonomyUtils


class NcbiTaxonomyTest(APITestCase):
    fixtures = ['ncbi_taxonomy_ncbi_taxaname', 'ncbi_taxonomy_ncbi_taxanode']
    multi_db = True

    def test_loaddata(self):
        self.assertEquals(NcbiTaxaNode.objects.all().count(), 20,
                          "There are 20 ncbi_taxa_nodes posts")
        node = NcbiTaxonomyUtils.fetch_node('33208')
        self.assertEquals(node.parent_id, 33154, 'got the correct parent id')
        self.assertEquals(node.left_index, 1937419, 'got the correct left index')
        self.assertEquals(node.right_index, 2978372, 'got the correct right index')

    def test_fetch_descendant_ids(self):
        results = NcbiTaxonomyUtils.fetch_descendant_ids('10090')
        self.assertEqual(len(results), 17, "Got back 17 descendant ids")
        expected_list = [10090, 10091, 10092, 35531, 39442, 46456, 57486, 80274, 116058, 179238,
                         477815, 477816, 947985, 1266728, 1385377, 1643390, 1879032]
        self.assertListEqual(expected_list, results, 'fetch_descendant_nodes ok. Both list contains the same ids')
