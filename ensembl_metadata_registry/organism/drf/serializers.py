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
from organism.models import Organism, OrganismAlias, OrganismPublication
from ensembl_metadata_registry.utils.drf_mixin import SerializerMixin


class OrganismAliasSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganismAlias
        fields = ('organism_alias_id', 'organism_id', 'alias', 'organism')


class OrganismPublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganismPublication
        fields = ('organism_publication_id', 'organism_id', 'publication', 'organism')


class OrganismSerializer(SerializerMixin, serializers.ModelSerializer):

    ONE2MANY_SERIALIZER = {Organism.ONE2MANY_RELATED['ORGANISM_ALIAS']: OrganismAliasSerializer,
                           Organism.ONE2MANY_RELATED['ORGANISM_PUBLICAION']:
                           OrganismPublicationSerializer}

    class Meta:
        model = Organism
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OrganismSerializer, self).__init__(*args, **kwargs)
        self.set_related_fields(OrganismSerializer, **kwargs)
