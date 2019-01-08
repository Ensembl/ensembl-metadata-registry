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


from ncbi_taxonomy.models import NcbiTaxaNode
from django.db import connections
from collections import namedtuple


class NcbiTaxonomyUtils(object):

    @classmethod
    def fetch_node(cls, taxon_id):
        print('Id from fetch node ' + str(taxon_id))
        node = NcbiTaxaNode.objects.get(pk=taxon_id)
        return node

    @classmethod
    def fetch_descendant_ids(cls, taxon_id):
        cursor = connections['ncbi_taxonomy'].cursor()
        sql = "SELECT n.taxon_id FROM ncbi_taxa_node n  JOIN ncbi_taxa_node parent ON " +\
            " (n.left_index BETWEEN parent.left_index AND parent.right_index AND n.taxon_id<>parent.taxon_id) " +\
              " WHERE parent.taxon_id=" + taxon_id
        cursor.execute(sql)
        results = [item[0] for item in cursor.fetchall()]
        results = [int(taxon_id)] + results
        return results

    @classmethod
    def dictfetchall(cls, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
            ]

    @classmethod
    def namedtuplefetchall(cls, cursor):
        "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]
