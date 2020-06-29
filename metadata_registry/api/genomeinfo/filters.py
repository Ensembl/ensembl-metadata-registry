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


from rest_framework.filters import BaseFilterBackend
from rest_framework.compat import coreapi
from metadata_registry.api.datarelease.filters import ensembl_genomes_version_field,\
    ensembl_version_field
from metadata_registry.utils.drf_filters import DrfFilters
from metadata_registry.models.genomeinfo import Genome
from django.db.models import Q
from metadata_registry.api.assembly.filters import assembly_level_field, assembly_name_field,\
    assembly_ucsc_field, assembly_accession_field
from metadata_registry.api.division.filters import division_name_field, division_short_name_field

# Fields
genome_id_field = coreapi.Field(
            name='genome_id',
            location='query',
            required=False,
            type='string',
            description='genome_id to filter(eg: 1)')

db_name_field = coreapi.Field(
            name='dbname',
            location='query',
            required=False,
            type='string',
            description='dbname to filter(eg: homo_sapiens_core)')

db_type_field = coreapi.Field(
            name='type',
            location='query',
            required=False,
            type='string',
            description='type to filter(eg: core, funcgen,variation,otherfeatures')

has_pan_compara_field = coreapi.Field(
            name='has_pan_compara',
            location='query',
            required=False,
            type='boolean',
            description='filter genomes which has_pan_compara  (eg. true, false)')

has_peptide_compara_field = coreapi.Field(
            name='has_peptide_compara',
            location='query',
            required=False,
            type='boolean',
            description='filter genomes which has_peptide_compara  (eg. true, false)')

has_synteny_field = coreapi.Field(
            name='has_synteny',
            location='query',
            required=False,
            type='boolean',
            description='filter genomes which has_synteny  (eg. true, false)')

has_variations_field = coreapi.Field(
            name='has_variations',
            location='query',
            required=False,
            type='boolean',
            description='filter genomes which has_variations  (eg. true, false)')

has_genome_alignments_field = coreapi.Field(
            name='has_genome_alignments',
            location='query',
            required=False,
            type='boolean',
            description='filter genomes which has_genome_alignments  (eg. true, false)')

has_genome_alignments_field = coreapi.Field(
            name='has_genome_alignments',
            location='query',
            required=False,
            type='boolean',
            description='filter genomes which has_genome_alignments  (eg. true, false)')

has_other_alignments_field = coreapi.Field(
            name='has_other_alignments',
            location='query',
            required=False,
            type='boolean',
            description='filter genomes which has_other_alignments  (eg. true, false)')


class GenomeExactMatchFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset

    def get_schema_fields(self, view):
        return [DrfFilters.get_exact_match_field(Genome)]


class GenomeExpandFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset

    def get_schema_fields(self, view):
        return [DrfFilters.get_expand_field(Genome),
                DrfFilters.get_expand_all_field(Genome)
                ]


class GenomeFilterBackend(BaseFilterBackend):
    """
    Filter to filter by genome attributes
    """
    def filter_queryset(self, request, queryset, view):

        genome_id = request.query_params.get('genome_id', None)
        if genome_id is not None:
            queryset = queryset.filter(genome_id=genome_id)

        has_genome_alignments = request.query_params.get('has_genome_alignments', None)
        if has_genome_alignments is not None:
            has_genome_alignments = int(1) if has_genome_alignments == 'true' else int(0)
            queryset = queryset.filter(has_genome_alignments=has_genome_alignments)

        has_other_alignments = request.query_params.get('has_other_alignments', None)
        if has_other_alignments is not None:
            has_other_alignments = int(1) if has_other_alignments == 'true' else int(0)
            queryset = queryset.filter(has_other_alignments=has_other_alignments)

        return queryset

    def get_schema_fields(self, view):
        return [genome_id_field, has_genome_alignments_field, has_other_alignments_field]


class GenomeDatabasereleaseFilterBackend(BaseFilterBackend):
    """
    Filter to filter by dbname, tye
    """
    def filter_queryset(self, request, queryset, view):
        dbname = request.query_params.get('dbname', None)
        if dbname is not None:
            queryset = queryset.filter(genome_database__dbname__icontains=dbname)

        dbtype = request.query_params.get('type', None)
        if dbtype is not None:
            queryset = queryset.filter(genome_database__type__icontains=dbtype)

        return queryset

    def get_schema_fields(self, view):
        return [db_name_field, db_type_field]


class GenomeDatareleaseFilterBackend(BaseFilterBackend):
    """
    Filter to filter by ensembl_version, ensembl_genomes_version from data_release.
    """
    def filter_queryset(self, request, queryset, view):
        # ensembl_version = request.query_params.get('ensembl_version', DataReleaseUtils.get_latest_ensembl_version())
        ensembl_version = request.query_params.get('ensembl_version', None)
        if ensembl_version is not None:
            queryset = queryset.filter(data_release__ensembl_version=ensembl_version)

        # ensembl_genomes_version = request.query_params.get('ensembl_genomes_version',
        #                                                   DataReleaseUtils.get_latest_ensemblgenomes_version())
        ensembl_genomes_version = request.query_params.get('ensembl_genomes_version',
                                                           None)
        if ensembl_genomes_version is not None:
            queryset = queryset.filter(data_release__ensembl_genomes_version=ensembl_genomes_version)

        return queryset

    def get_schema_fields(self, view):
        return [ensembl_version_field, ensembl_genomes_version_field]


class GenomeDivisionFilterBackend(BaseFilterBackend):
    """
    Filter to filter by division
    """
    def filter_queryset(self, request, queryset, view):
        division_name = request.query_params.get('division_name', None)
        if division_name is not None:
            if division_name.lower() == 'ensemblgenomes':
                queryset = queryset.filter(Q(division__name__iexact="EnsemblMetazoa") |
                                           Q(division__name__iexact="EnsemblFungi") |
                                           Q(division__name__iexact="EnsemblBacteria") |
                                           Q(division__name__iexact="EnsemblProtists") |
                                           Q(division__name__iexact="EnsemblPlants"))
            else:
                queryset = queryset.filter(division__name__iexact=division_name)

        short_name = request.query_params.get('short_name', None)
        if short_name is not None:
            queryset = queryset.filter(division__short_name__icontains=short_name)

        return queryset

    def get_schema_fields(self, view):
        return [division_name_field, division_short_name_field]


class GenomeAssemblyFilterBackend(BaseFilterBackend):
    """
    Filter to filter by assembly_name, assembly_level, assembly_ucsc, assembly_accession
    """
    def filter_queryset(self, request, queryset, view):
        assembly_name = request.query_params.get('assembly_name', None)
        if assembly_name is not None:
            queryset = queryset.filter(assembly__assembly_name__icontains=assembly_name)

        assembly_level = request.query_params.get('assembly_level', None)
        if assembly_level is not None:
            queryset = queryset.filter(assembly__assembly_level__icontains=assembly_level)

        assembly_ucsc = request.query_params.get('assembly_ucsc', None)
        if assembly_ucsc is not None:
            queryset = queryset.filter(assembly__assembly_ucsc__icontains=assembly_ucsc)

        assembly_accession = request.query_params.get('assembly_accession', None)
        if assembly_accession is not None:
            queryset = queryset.filter(assembly__assembly_accession__iexact=assembly_accession)

        return queryset

    def get_schema_fields(self, view):
        return [assembly_name_field, assembly_level_field, assembly_ucsc_field, assembly_accession_field]


class GenomeComparaFilterBackend(BaseFilterBackend):
    """
    Filter to filter by has_*_compara.
    """
    def filter_queryset(self, request, queryset, view):
        has_pan_compara = request.query_params.get('has_pan_compara', None)
        if has_pan_compara is not None:
            has_pan_compara = int(1) if has_pan_compara == 'true' else int(0)
            queryset = queryset.filter(has_pan_compara=has_pan_compara)

        has_peptide_compara = request.query_params.get('has_peptide_compara', None)
        if has_peptide_compara is not None:
            has_peptide_compara = int(1) if has_peptide_compara == 'true' else int(0)
            queryset = queryset.filter(has_peptide_compara=has_peptide_compara)

        return queryset

    def get_schema_fields(self, view):
        return [has_pan_compara_field, has_peptide_compara_field]


class GenomeVariationFilterBackend(BaseFilterBackend):
    """
    Filter to filter by has_variations.
    """
    def filter_queryset(self, request, queryset, view):
        has_variations = request.query_params.get('has_variations', None)
        if has_variations is not None:
            has_variations = int(1) if has_variations == 'true' else int(0)
            queryset = queryset.filter(has_variations=has_variations)

        return queryset

    def get_schema_fields(self, view):
        return [has_variations_field]
