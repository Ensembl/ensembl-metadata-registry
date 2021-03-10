from rest_framework import serializers
from ensembl_metadata.models.assembly import Assembly, AssemblySequence


class AssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = Assembly
        exclude = ['assembly_id', 'assembly_default']


class AssemblySequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssemblySequence
        exclude = ['assembly', 'assembly_sequence_id']
