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

import coreapi
from django.db.models import Q
from rest_framework.filters import BaseFilterBackend

from metadata_registry.models.organism import Organism
from metadata_registry.utils.drf_filters import DrfFilters
from ncbi_taxonomy.utils import NcbiTaxonomyUtils

# core api fields for filtering
organism_name_field = coreapi.Field(name='organism_name',
                                    location='query',
                                    required=False,
                                    type='string',
                                    description='organism_name to filter(eg: homo_sapiens)')

display_name_field = coreapi.Field(name='display_name',
                                   location='query',
                                   required=False,
                                   type='string',
                                   description='display_name to filter(eg: human)')

any_name_field = coreapi.Field(name='any_name',
                               location='query',
                               required=False,
                               type='string',
                               description='any_name (organism_name or display_name) to filter (eg: homo)')  # @IgnorePep8

organism_alias_field = coreapi.Field(name='organism_alias',
                                     location='query',
                                     required=False,
                                     type='string',
                                     description='organism_alias to filter(eg: h_sapiens eg: hsapiens)')

organism_id_field = coreapi.Field(name='organism_id',
                                  location='query',
                                  required=False,
                                  type='integer',
                                  description='organism_id to filter(eg: 1)')

taxonomy_id_field = coreapi.Field(name='taxonomy_id',
                                  location='query',
                                  required=False,
                                  type='integer',
                                  description='taxonomy_id to filter (eg: 9606)')

taxonomy_ids_field = coreapi.Field(name='taxonomy_ids',
                                   location='query',
                                   required=False,
                                   type='string',
                                   description='taxonomy_ids to filter (eg: 9606, 10090)')

taxonomy_branch_field = coreapi.Field(name='taxonomy_branch',
                                      location='query',
                                      required=False,
                                      type='string',
                                      description='taxonomy_branch to filter (eg: 10090)')


class OrganismExpandFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset

    def get_schema_fields(self, view):
        return [DrfFilters.get_expand_field(Organism), DrfFilters.get_expand_all_field(Organism)]


class OrganismFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        # Filter to filter by organism_name.
        organism_name = request.query_params.get('organism_name', None)
        if organism_name is not None:
            queryset = queryset.filter(name__icontains=organism_name)

        # Filter to filter by display_name.
        display_name = request.query_params.get('display_name', None)
        if display_name is not None:
            queryset = queryset.filter(display_name__icontains=display_name)

        # Filter to filter by any name
        any_name = request.query_params.get('any_name', None)
        if any_name is not None:
            queryset = queryset.filter(Q(name__icontains=any_name) | Q(display_name__icontains=any_name))
        return queryset

    def get_schema_fields(self, view):
        return [organism_name_field, display_name_field, any_name_field]


class OrganismOrganismAliasFilterBackend(BaseFilterBackend):
    """
    Filter to filter by organism alias_name.
    """

    def filter_queryset(self, request, queryset, view):
        organism_alias = request.query_params.get('organism_alias', None)
        if organism_alias is not None:
            queryset = queryset.filter(organism_alias__alias=organism_alias)
        return queryset

    def get_schema_fields(self, view):
        return [organism_alias_field]


class OrganismAliasOrganismFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        # Exact or fuzzy
        exact_match = request.query_params.get('exact_match', None)

        # Filter to filter by organism_name.
        organism_name = request.query_params.get('organism_name', None)
        if organism_name is not None:
            if exact_match is not None and exact_match == "true":
                queryset = queryset.filter(organism__name__iexact=organism_name)
            else:
                queryset = queryset.filter(organism__name__icontains=organism_name)

        # Filter to filter by display_name.
        display_name = request.query_params.get('display_name', None)
        if display_name is not None:
            if exact_match is not None and exact_match == "true":
                queryset = queryset.filter(organism__display_name__iexact=display_name)
            else:
                queryset = queryset.filter(organism__display_name__icontains=display_name)

        # Filter to filter by any name
        any_name = request.query_params.get('any_name', None)
        if any_name is not None:
            if exact_match is not None and exact_match == "true":
                queryset = queryset.filter(
                    Q(organism__name__iexact=any_name) | Q(organism__display_name__iexact=any_name))  # @IgnorePep8
            else:
                queryset = queryset.filter(Q(organism__name__icontains=any_name) | Q(
                    organism__display_name__icontains=any_name))  # @IgnorePep8

        # Filter to filter by organism_id
        organism_id = request.query_params.get('organism_id', None)
        if organism_id is not None:
            queryset = queryset = queryset.filter(organism_id=organism_id)

        # Filter to filter by taxonomy_id.
        taxonomy_ids = request.query_params.get('taxonomy_ids', None)
        if taxonomy_ids is not None:
            taxonomy_ids_list = taxonomy_ids.split(',') if taxonomy_ids else None
            taxonomy_ids_list = [tax_id.strip() for tax_id in taxonomy_ids_list]
            queryset = queryset.filter(organism__taxonomy_id__in=taxonomy_ids_list)

        taxonomy_branch = request.query_params.get('taxonomy_branch', None)
        if taxonomy_branch is not None:
            taxonomy_ids_list = NcbiTaxonomyUtils.fetch_descendant_ids(taxonomy_branch)
            queryset = queryset.filter(organism__taxonomy_id__in=taxonomy_ids_list)

        organism_alias = request.query_params.get('organism_alias', None)
        if organism_alias is not None:
            queryset = queryset.filter(organism__organism_alias__alias=organism_alias)
        return queryset

        return queryset

    def get_schema_fields(self, view):
        return [organism_name_field, display_name_field, any_name_field,
                organism_id_field, organism_alias_field, taxonomy_ids_field, taxonomy_branch_field]


class OrganismPublicationOrganismFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        # Filter to filter by organism_name.
        organism_name = request.query_params.get('organism_name', None)
        if organism_name is not None:
            queryset = queryset.filter(organism__name__icontains=organism_name)

        # Filter to filter by display_name.
        display_name = request.query_params.get('display_name', None)
        if display_name is not None:
            queryset = queryset.filter(organism__display_name__icontains=display_name)

        # Filter to filter by any name
        any_name = request.query_params.get('any_name', None)
        if any_name is not None:
            queryset = queryset.filter(
                Q(organism__name__icontains=any_name) | Q(organism__display_name__icontains=any_name))

        organism_id = request.query_params.get('organism_id', None)
        if organism_id is not None:
            queryset = queryset = queryset.filter(organism_id=organism_id)
        return queryset

    def get_schema_fields(self, view):
        return [organism_name_field, display_name_field, any_name_field, organism_id_field]


class OganismTaxonomyFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        # Filter to filter by taxonomy_id.
        taxonomy_ids = request.query_params.get('taxonomy_ids', None)
        if taxonomy_ids is not None:
            ids = [int(taxid.strip()) for taxid in taxonomy_ids.split(',')]
            queryset = queryset.filter(taxonomy_id__in=ids)

        # Filter to filter by taxnomy_node.
        taxonomy_branch = request.query_params.get('taxonomy_branch', None)
        if taxonomy_branch is not None:
            descendant_tax_ids = NcbiTaxonomyUtils.fetch_descendant_ids(taxonomy_branch)
            queryset = queryset.filter(taxonomy_id__in=descendant_tax_ids)

        return queryset

    def get_schema_fields(self, view):
        return [taxonomy_ids_field, taxonomy_branch_field]
