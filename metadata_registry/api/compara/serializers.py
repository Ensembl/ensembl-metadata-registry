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

from rest_framework import serializers
from metadata_registry.models.compara import ComparaAnalysis, ComparaAnalysisEvent
from metadata_registry.utils.drf_mixin import SerializerMixin


class ComparaAnalysisSerializer(SerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = ComparaAnalysis
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ComparaAnalysisSerializer, self).__init__(*args, **kwargs)
        self.set_related_fields(ComparaAnalysisSerializer, **kwargs)


class ComparaAnalysisEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComparaAnalysisEvent
        fields = '__all__'
