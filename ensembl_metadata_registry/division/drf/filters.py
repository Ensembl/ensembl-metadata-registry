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
from division.utils import DivisionUtils

# Fields
division_name_field = coreapi.Field(
            name='division_name',
            location='query',
            required=False,
            type='string',
            description='division_name to filter(eg: ' + ",".join(DivisionUtils.get_all_division_names()) + ')'
            )

division_short_name_field = coreapi.Field(
            name='short_name',
            location='query',
            required=False,
            type='string',
            description='short_name to filter(eg: ' + ",".join(DivisionUtils.get_all_division_short_names()) + ')'
            )


class DivisionFilterBackend(BaseFilterBackend):
    """
    Filter to filter by division_name, short_name.
    """
    def filter_queryset(self, request, queryset, view):
        division_name = request.query_params.get('division_name', None)
        if division_name is not None:
            queryset = queryset.filter(name=division_name)

        short_name = request.query_params.get('short_name', None)
        if short_name is not None:
            queryset = queryset.filter(short_name__icontains=short_name)

        return queryset

    def get_schema_fields(self, view):
        return [division_name_field, division_short_name_field]
