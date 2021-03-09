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


from rest_framework.test import APITestCase
from metadata_registry.models.genomeinfo import Genome
from metadata_registry.utils.drf_utils import DrfUtils


class GenomeinfoMetaTest(APITestCase):
    """Tests to check _meta info"""


    def test_get_related_entities(self):
        one2many = DrfUtils.get_related_entities(Genome, 'one2many')
        one2many_expected = ['genome_feature', 'genome_event', 'genome_annotation', 'genome_variation',
                             'genome_database', 'genome_compara_analysis', 'genome_alignment']
        self.assertListEqual(sorted(one2many), sorted(one2many_expected))

        many2one = DrfUtils.get_related_entities(Genome, 'many2one')
        expected_many2one = ['assembly', 'organism', 'division']
        self.assertListEqual(sorted(many2one), sorted(expected_many2one))

        many2many = DrfUtils.get_related_entities(Genome, 'many2many')
        expected_many2many = ['assembly', 'organism', 'division']
        self.assertListEqual(sorted(many2many), sorted(expected_many2many))

        many2one = DrfUtils.get_related_entities(Genome)
        expected_many2one = ['assembly', 'organism', 'division', 'genome_feature', 'genome_event',
                             'genome_annotation', 'genome_variation', 'genome_database',
                             'genome_compara_analysis', 'genome_alignment']
        self.assertListEqual(sorted(many2one), sorted(expected_many2one))
