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


from django.test import TestCase
from ensembl_metadata_registry.utils.schema_utils import SchemaUtils


class UtilsTestCase(TestCase):
    def setUp(self):
        pass

    def test_get_field_names(self):
        field_names_datarelease = SchemaUtils.get_field_names("datarelease", "datarelease")
        expected_fields_datarelease = ['data_release_id', 'ensembl_version', 'ensembl_genomes_version',
                                       'release_date', 'is_current']
        self.assertListEqual(expected_fields_datarelease, field_names_datarelease,
                             "Got the right fields names for datarelease")

        field_names_genomeinfo = SchemaUtils.get_field_names("genomeinfo", "genome")
        expected_fields_genomeinfo = ['genome_id', 'genebuild', 'has_pan_compara', 'has_variations',
                                      'has_peptide_compara', 'has_genome_alignments', 'has_synteny',
                                      'has_other_alignments']
        self.assertListEqual(expected_fields_genomeinfo, field_names_genomeinfo,
                             "Got the right fields names for genomeinfo")

    def test_get_app_model_mappings(self):
        mappings = SchemaUtils.get_app_model_mappings()
        self.assertIn('genomeinfo', mappings['genome'], "Found model genome in genomeinfo app")
        self.assertIn('datarelease', mappings['datarelease'], "Found model datarelease in datarelease app")
