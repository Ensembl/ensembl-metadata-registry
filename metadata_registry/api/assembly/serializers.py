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

from rest_framework import serializers
from metadata_registry.models.assembly import Assembly, AssemblySequence
from metadata_registry.utils.drf_mixin import SerializerMixin


class AssemblySequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssemblySequence
        fields = '__all__'


class AssemblySerializer(SerializerMixin, serializers.ModelSerializer):

    ONE2MANY_SERIALIZER = {Assembly.ONE2MANY_RELATED['ASSEMBLY_SEQUENCE']: AssemblySequenceSerializer}

    class Meta:
        model = Assembly
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AssemblySerializer, self).__init__(*args, **kwargs)
        self.set_related_fields(AssemblySerializer, **kwargs)
