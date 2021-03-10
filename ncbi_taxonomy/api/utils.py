from django.db import connections
from ncbi_taxonomy.models import TaxonomyNode


class TaxonomyUtils(object):

    @classmethod
    def fetch_node(cls, taxon_id):
        node = TaxonomyNode.objects.get(pk=taxon_id)
        return node

    @classmethod
    def fetch_descendent_ids(cls, taxon_ids):
        cursor = connections['ncbi_taxonomy'].cursor()
        sql = "SELECT n.taxon_id FROM ncbi_taxa_node n  JOIN ncbi_taxa_node parent ON " + \
              " (n.left_index BETWEEN parent.left_index AND parent.right_index) " + \
              " WHERE parent.taxon_id IN (" + str(taxon_ids) + ")"
        cursor.execute(sql)
        results = [item[0] for item in cursor.fetchall()]
        return results
