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
from datarelease.models import DataRelease, DataReleaseDatabase,\
    DataReleaseDatabaseEvent


class DataReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRelease
        fields = '__all__'


class DataReleaseDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataReleaseDatabase
        fields = '__all__'


class DataReleaseDatabaseEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataReleaseDatabaseEvent
        fields = '__all__'
