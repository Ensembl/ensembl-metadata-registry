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

from rest_framework.filters import BaseFilterBackend
from rest_framework.compat import coreapi
from datarelease.utils import DataReleaseUtils

# Fields
ensembl_version_field = coreapi.Field(
            name='ensembl_version',
            location='query',
            required=False,
            type='integer',
            description='ensembl_version to filter(eg: ' + str(DataReleaseUtils.get_latest_ensembl_version()) + ' )')

ensembl_genomes_version_field = coreapi.Field(
            name='ensembl_genomes_version',
            location='query',
            required=False,
            type='integer',
            description='ensembl_genomes_version to filter(eg: ' +
            str(DataReleaseUtils.get_latest_ensemblgenomes_version()) + ' )')


class DatareleaseFilterBackend(BaseFilterBackend):
    """
    Filter to filter by ensembl_version, ensembl_genomes_version.
    """
    def filter_queryset(self, request, queryset, view):
        ensembl_version = request.query_params.get('ensembl_version', None)
        if ensembl_version is not None:
            queryset = queryset.filter(ensembl_version=ensembl_version)

        ensembl_genomes_version = request.query_params.get('ensembl_genomes_version', None)
        if ensembl_genomes_version is not None:
            queryset = queryset.filter(ensembl_genomes_version=ensembl_genomes_version)

        return queryset

    def get_schema_fields(self, view):
        return [ensembl_version_field, ensembl_genomes_version_field]
