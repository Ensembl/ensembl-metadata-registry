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
from ensembl_metadata_registry.utils.drf_filters import DrfFilters
from assembly.models import Assembly

# Fields
assembly_name_field = coreapi.Field(
            name='assembly_name',
            location='query',
            required=False,
            type='string',
            description='assembly_name to filter(eg: GRCh38)')

assembly_accession_field = coreapi.Field(
            name='assembly_accession',
            location='query',
            required=False,
            type='string',
            description='assembly_accession to filter(eg: GCA_000001405.22)')

assembly_sequence_acc_field = coreapi.Field(
            name='sequence_accession',
            location='query',
            required=False,
            type='string',
            description='sequence_accession to filter(eg: HT000001)')

assembly_level_field = coreapi.Field(
            name='assembly_level',
            location='query',
            required=False,
            type='string',
            description='assembly_level to filter(eg: chromosome)')

assembly_ucsc_field = coreapi.Field(
            name='assembly_ucsc',
            location='query',
            required=False,
            type='string',
            description='assembly_ucsc to filter(eg: hg38, mm10, rn6 )')


class AssemblyExpandFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset

    def get_schema_fields(self, view):
        return [DrfFilters.get_expand_field(Assembly), DrfFilters.get_expand_all_field(Assembly)]


class AssemblyFilterBackend(BaseFilterBackend):
    """
    Filter to filter by assembly_name, assembly_level, assembly_accession
    """
    def filter_queryset(self, request, queryset, view):
        assembly_name = request.query_params.get('assembly_name', None)
        if assembly_name is not None:
            queryset = queryset.filter(assembly_name__icontains=assembly_name)

        assembly_level = request.query_params.get('assembly_level', None)
        if assembly_level is not None:
            queryset = queryset.filter(assembly_level__icontains=assembly_level)

        assembly_accession = request.query_params.get('assembly_accession', None)
        if assembly_accession is not None:
            queryset = queryset.filter(assembly_accession__icontains=assembly_accession)

        assembly_ucsc = request.query_params.get('assembly_ucsc', None)
        if assembly_ucsc is not None:
            queryset = queryset.filter(assembly_ucsc__icontains=assembly_ucsc)

        return queryset

    def get_schema_fields(self, view):
        return [assembly_name_field, assembly_level_field, assembly_accession_field, assembly_ucsc_field]


class AssemblySequenceFilterBackend(BaseFilterBackend):
    """
    Filter to filter by assembly_name and acc
    """
    def filter_queryset(self, request, queryset, view):

        sequence_accession = request.query_params.get('sequence_accession', None)
        if sequence_accession is not None:
            queryset = queryset.filter(acc__icontains=sequence_accession)

        assembly_name = request.query_params.get('assembly_name', None)
        if assembly_name is not None:
            queryset = queryset.filter(assembly__assembly_name__icontains=assembly_name)
        return queryset

    def get_schema_fields(self, view):
        return [assembly_name_field, assembly_sequence_acc_field]
