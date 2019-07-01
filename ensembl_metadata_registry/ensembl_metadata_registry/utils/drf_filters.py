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

from django_filters.compat import coreapi
from ensembl_metadata_registry.utils.drf_utils import DrfUtils


class DrfFilters(object):

    @classmethod
    def get_expand_field(cls, model):

        related_models = DrfUtils.get_related_entities(model)
        counter = 1
        description_ = "comma separated list of objects to expand (eg:<br/> "
        for _model in related_models:
            if counter > 5:
                description_ = description_ + _model + ',<br/>'
                counter = 1
            else:
                description_ += _model + ','
                counter += 1
        description_ += ")"

        expand_field = coreapi.Field(
                name='expand',
                location='query',
                required=False,
                type='string',
                description=description_)
        return expand_field

    @classmethod
    def get_expand_all_field(cls, model):
        expand_all_field = coreapi.Field(
            name='expand_all',
            location='query',
            required=False,
            type='boolean',
            description='selecting true will expand all the related fields, to selectively expand, use expand above')
        return expand_all_field

    @classmethod
    def get_exact_match_field(cls, model):
        expand_all_field = coreapi.Field(
            name='exact_match',
            location='query',
            required=False,
            type='boolean',
            description='selecting true will attempt to match the exact search query')
        return expand_all_field
