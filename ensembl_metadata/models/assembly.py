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

    class Meta:
        managed = True
        db_table = 'assembly_sequence'
        unique_together = (('assembly', 'name', 'acc'),)


class AssemblyKaryotype(models.Model):
    assembly_karyotype_id = models.AutoField(primary_key=True)
    assembly = models.ForeignKey(Assembly, models.CASCADE, related_name='karyotypes')
    region_name = models.CharField(max_length=40)
    region_start = models.IntegerField()
    region_end = models.IntegerField()
    band = models.CharField(max_length=50)
    strain = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'assembly_karyotype'
