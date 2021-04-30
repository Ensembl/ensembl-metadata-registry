from rest_framework import serializers
from ensembl_metadata.models.assembly import Assembly, AssemblySequence


class AssemblySerializer(serializers.ModelSerializer):
    class Meta:
        model = Assembly
        exclude = ['assembly_id']


class AssemblySequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssemblySequence
        exclude = ['assembly_sequence_id', 'assembly']
