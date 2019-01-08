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


from rest_framework.filters import BaseFilterBackend
from ncbi_taxonomy.utils import NcbiTaxonomyUtils
from organism.drf.filters import taxonomy_branch_field, taxonomy_ids_field


class TaxonomyFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        # Filter to filter by taxonomy_id.
        taxonomy_ids = request.query_params.get('taxonomy_ids', None)
        if taxonomy_ids is not None:
            ids = [int(taxid.strip()) for taxid in taxonomy_ids.split(',')]
            queryset = queryset.filter(taxon_id__in=ids)

        # Filter to filter by taxnomy_node.
        taxonomy_branch = request.query_params.get('taxonomy_branch', None)
        if taxonomy_branch is not None:
            descendant_tax_ids = NcbiTaxonomyUtils.fetch_descendant_ids(taxonomy_branch)
            print(descendant_tax_ids)
            queryset = queryset.filter(taxon_id__in=descendant_tax_ids)

        return queryset

    def get_schema_fields(self, view):
        return [taxonomy_ids_field, taxonomy_branch_field]
