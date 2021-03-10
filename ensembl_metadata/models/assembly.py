from django.db import models


class Assembly(models.Model):
    assembly_id = models.AutoField(primary_key=True)
    assembly_accession = models.CharField(unique=True, max_length=16, blank=True, null=True)
    assembly_name = models.CharField(max_length=200)
    assembly_default = models.CharField(max_length=200)
    assembly_ucsc = models.CharField(max_length=16, blank=True, null=True)
    assembly_level = models.CharField(max_length=50)
    base_count = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'assembly'


class AssemblySequence(models.Model):
    assembly_sequence_id = models.AutoField(primary_key=True)
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE, related_name='sequences')
    name = models.CharField(max_length=40)
    acc = models.CharField(max_length=24, blank=True, null=True)
    sequence_location = models.CharField(max_length=10, default='SO:0000738')
    length = models.IntegerField(default=0)  # default to be removed once we have fully migrated to new schema
    chromosomal = models.BooleanField(default=False)  # default to be removed once we have fully migrated to new schema

    class Meta:
        managed = True
        db_table = 'assembly_sequence'
        unique_together = (('assembly', 'name'),)
