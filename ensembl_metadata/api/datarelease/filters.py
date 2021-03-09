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
from metadata_registry.utils.datarelease import DataReleaseUtils

# Fields
version_field = coreapi.Field(
            name='version',
            location='query',
            required=False,
            type='integer',
            description='version to filter(eg: ' + str(DataReleaseUtils.get_latest_version()) + ' )')

is_current_field = coreapi.Field(
            name='is_current',
            location='query',
            required=False,
            type='integer',
            description='filter releases on is_current flag (eg: 0 or 1  )')


class DatareleaseFilterBackend(BaseFilterBackend):
    """
    Filter to filter by ensembl_version.
    """
    def filter_queryset(self, request, queryset, view):
        version = request.query_params.get('version', None)
        if version is not None:
            queryset = queryset.filter(version=version)

        is_current = request.query_params.get('is_current', None)
        if is_current is not None:
            queryset = queryset.filter(is_current=is_current)

        return queryset

    def get_schema_fields(self, view):
        return [version_field, is_current_field]
