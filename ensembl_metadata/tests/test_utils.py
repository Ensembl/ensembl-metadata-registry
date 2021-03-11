from django.test import TestCase
from rest_framework.test import APITestCase

from ensembl_metadata.models.genome import Division
from ensembl_metadata.utils.division import DivisionUtils
from ensembl_metadata.models.datarelease import DataRelease
from ensembl_metadata.utils.datarelease import DataReleaseUtils
from ensembl_metadata.utils.schema_utils import SchemaUtils


"""
class DataReleaseUtilsTest(APITestCase):
    fixtures = ['data_release']
    multi_db = True

    def test_loaddata(self):
        datarelease = DataRelease.objects.get(pk=1)
        self.assertEqual(1, datarelease.data_release_id)
        self.assertEqual(80, datarelease.version)

        all_ = DataRelease.objects.all()
        self.assertEquals(len(all_), 5)

    def test_get_latest_version(self):
        version = DataReleaseUtils.get_latest_version()
        self.assertEqual(96, version, "Got the right version")


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


class UtilsTestCase(TestCase):
    def setUp(self):
        pass

    def test_get_field_names(self):
        field_names_datarelease = SchemaUtils.get_field_names("metadata_registry", "datarelease")
        expected_fields_datarelease = ['data_release_id', 'label', 'version',
                                       'release_date', 'is_current']
        self.assertListEqual(expected_fields_datarelease, field_names_datarelease,
                             "Got the right fields names for datarelease")

        field_names_genomeinfo = SchemaUtils.get_field_names("metadata_registry", "genome")
        expected_fields_genomeinfo = ['genome_id', 'genome_uuid', 'genebuild', 'has_pan_compara', 'has_variation',
                                      'has_microarray', 'has_peptide_compara', 'has_genome_alignments', 'has_synteny',
                                      'has_other_alignments','created']
        self.assertListEqual(expected_fields_genomeinfo, field_names_genomeinfo,
                             "Got the right fields names for genomeinfo")

    def test_get_app_model_mappings(self):
        mappings = SchemaUtils.get_app_model_mappings()
        self.assertIn('metadata_registry', mappings['genome'], "Found model genome in metadata_registry app")
        self.assertIn('metadata_registry', mappings['datarelease'], "Found model datarelease in metadata_registry app")
"""
