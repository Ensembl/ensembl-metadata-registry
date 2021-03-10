from rest_framework.test import APITestCase
from ncbi_taxonomy.models import TaxonomyName, TaxonomyNode
from ncbi_taxonomy.api.utils import TaxonomyUtils


class TaxonomyTest(APITestCase):
    databases = {'ncbi_taxonomy'}
    fixtures = ['taxonomy_name', 'taxonomy_node']

    def test_load_name(self):
        self.assertEquals(TaxonomyName.objects.all().count(), 21, 'Fetched all taxonomy names')
        taxonomy_names = TaxonomyName.objects.filter(taxon_id=10090, name_class='scientific name')
        taxonomy_name = taxonomy_names[0]
        self.assertEquals(taxonomy_name.name, 'Mus musculus', 'Correct scientific name')

    def test_load_node(self):
        self.assertEquals(TaxonomyNode.objects.all().count(), 19, 'Fetched all taxonomy nodes')
        taxonomy_node = TaxonomyUtils.fetch_node(33208)
        self.assertEquals(taxonomy_node.parent_id, 1, 'Correct parent id')
        taxonomy_names = taxonomy_node.names()
        names = []
        for name in taxonomy_names:
            names.append(name.name)
        self.assertListEqual(names, ['Animalia', 'metazoans', 'multicellular animals'], 'Correct names')

    def test_fetch_descendant_ids(self):
        results = TaxonomyUtils.fetch_descendent_ids('10090')
        self.assertEqual(len(results), 17, 'Fetched all descendent nodes')
        expected_list = [10090, 10091, 10092, 35531, 39442, 46456, 57486, 80274, 116058, 179238,
                         477815, 477816, 947985, 1266728, 1385377, 1643390, 1879032]
        self.assertListEqual(expected_list, results, 'Correct descendent taxon ids')
