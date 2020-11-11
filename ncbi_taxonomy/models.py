"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from django.db import models


class NcbiTaxaNode(models.Model):
    ONE2MANY_RELATED = {'NCBI_TAXA_NAME': 'ncbi_taxa_name'}

    taxon_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    rank = models.CharField(max_length=32)
    genbank_hidden_flag = models.IntegerField()
    left_index = models.IntegerField()
    right_index = models.IntegerField()
    root_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ncbi_taxa_node'


class NcbiTaxaName(models.Model):
    MANY2ONE_RELATED = {'NCBI_TAXA_NODE': 'ncbi_taxa_node'}

    taxon_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    name_class = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ncbi_taxa_name'
        unique_together = (('taxon_id', 'name', 'name_class'),)
