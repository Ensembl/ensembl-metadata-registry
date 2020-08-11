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


from metadata_registry_current.models.division import Division


class DivisionUtils(object):

    @classmethod
    def get_all_division_names(cls, eg_only=False):
        division = Division.objects.all()

        if division is not None:
            if eg_only is True:
                all_divisions = list(division.values_list('name', flat=True))
                eg_only_divisions = [div for div in all_divisions if div.lower() not in ['ensembl', 'ensemblgenomes']]
                return eg_only_divisions
            else:
                return list(division.values_list('name', flat=True))

        return None

    @classmethod
    def get_all_division_short_names(cls, eg_only=False):
        division = Division.objects.all()

        if division is not None:
            if eg_only is True:
                pass
            else:
                return list(division.values_list('short_name', flat=True))

        return None
