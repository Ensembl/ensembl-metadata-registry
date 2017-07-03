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
from compara.models import ComparaAnalysis

# Fields
genome_id_field = coreapi.Field(
            name='genome_id',
            location='query',
            required=False,
            type='integer',
            description='genome_id to filter(eg: 1)')


class ComparaExpandFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset

    def get_schema_fields(self, view):
        return [DrfFilters.get_expand_field(ComparaAnalysis), DrfFilters.get_expand_all_field(ComparaAnalysis)]


class ComparaFilterBackend(BaseFilterBackend):
    """
    Filter to filter by genome_id
    """
    def filter_queryset(self, request, queryset, view):
        genome_id = request.query_params.get('genome_id', None)
        if genome_id is not None:
            queryset = queryset.filter(genome_id=genome_id)

        return queryset

    def get_schema_fields(self, view):
        return [genome_id_field]
