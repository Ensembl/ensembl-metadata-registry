from django.db import models
from ensembl_metadata.models.assembly import Assembly
from ensembl_metadata.models.datarelease import DataRelease
from ensembl_metadata.models.organism import Organism
import uuid


class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    short_name = models.CharField(unique=True, max_length=8)


class Genome(models.Model):
    genome_id = models.IntegerField(primary_key=True)
    genome_uuid = models.CharField(max_length=128, default=uuid.uuid1, unique=True)
    assembly = models.ForeignKey(Assembly, models.CASCADE, related_name='genomes')
    organism = models.ForeignKey(Organism, models.CASCADE, related_name='genomes')
    genebuild = models.CharField(max_length=255)
    has_pan_compara = models.BooleanField()
    has_variation = models.BooleanField()
    has_microarray = models.BooleanField()
    has_peptide_compara = models.BooleanField()
    has_genome_alignments = models.BooleanField()
    has_synteny = models.BooleanField()
    has_other_alignments = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)


class GenomeDatabase(models.Model):
    genome_database_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='databases')
    dbname = models.CharField(max_length=64)
    species_id = models.IntegerField()
    type = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        unique_together = (('dbname', 'species_id', 'genome'),)


class GenomeAlignment(models.Model):
    genome_alignment_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='alignments')
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    count = models.IntegerField()
    genome_database = models.ForeignKey(GenomeDatabase, on_delete=models.CASCADE,
                                        related_name='alignments')

    class Meta:
        unique_together = (('genome', 'type', 'name', 'genome_database'),)


class GenomeAnnotation(models.Model):
    genome_annotation_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='annotations')
    type = models.CharField(max_length=32)
    value = models.CharField(max_length=128)
    genome_database = models.ForeignKey(GenomeDatabase, on_delete=models.CASCADE,
                                        related_name='annotations')

    class Meta:
        unique_together = (('genome', 'type', 'genome_database'),)


class GenomeDivision(models.Model):
    genome_division_id = models.AutoField(primary_key=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE,
                                 related_name='divisions')
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='divisions')


class GenomeEvent(models.Model):
    genome_event_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='events')
    type = models.CharField(max_length=32)
    source = models.CharField(max_length=128, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)


class GenomeFeature(models.Model):
    genome_feature_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='features')
    type = models.CharField(max_length=32)
    analysis = models.CharField(max_length=128)
    count = models.IntegerField()
    genome_database = models.ForeignKey(GenomeDatabase, models.CASCADE,
                                        related_name='features')

    class Meta:
        unique_together = (('genome', 'type', 'analysis', 'genome_database'),)


class GenomeRelease(models.Model):
    genome_release_id = models.AutoField(primary_key=True)
    genome_uuid = models.ForeignKey(Genome, on_delete=models.CASCADE,
                                    related_name='releases',
                                    to_field='genome_uuid')
    division = models.ForeignKey(Division, on_delete=models.CASCADE,
                                 related_name='releases')
    data_release = models.ForeignKey(DataRelease, on_delete=models.CASCADE,
                                     related_name='releases')


class GenomeVariation(models.Model):
    genome_variation_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='variations')
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    count = models.IntegerField()
    genome_database = models.ForeignKey(GenomeDatabase, on_delete=models.CASCADE,
                                        related_name='variations')

    class Meta:
        unique_together = (('genome', 'type', 'name', 'genome_database'),)


class ComparaAnalysis(models.Model):
    compara_analysis_id = models.AutoField(primary_key=True)
    genome_compara_analysis = models.ManyToManyField('ensembl_metadata.Genome',
                                                     through='GenomeComparaAnalysis')
    method = models.CharField(max_length=50)
    set_name = models.CharField(max_length=128, blank=True, null=True)
    dbname = models.CharField(max_length=64)
    data_release = models.ForeignKey(DataRelease, on_delete=models.CASCADE,
                                     related_name='analyses')
    division = models.ForeignKey(Division, on_delete=models.CASCADE,
                                 related_name='analyses')

    class Meta:
        unique_together = (('division', 'method', 'set_name', 'dbname'),)


class ComparaAnalysisEvent(models.Model):
    compara_analysis_event_id = models.AutoField(primary_key=True)
    compara_analysis = models.ForeignKey('ComparaAnalysis', on_delete=models.CASCADE,
                                         related_name='events')
    type = models.CharField(max_length=32)
    source = models.CharField(max_length=128, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True)


class GenomeComparaAnalysis(models.Model):
    genome_compara_analysis_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='analyses')
    compara_analysis = models.ForeignKey(ComparaAnalysis, on_delete=models.CASCADE,
                                         related_name='analyses')

    class Meta:
        unique_together = (('genome', 'compara_analysis'),)
