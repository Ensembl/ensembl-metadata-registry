# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Assembly(models.Model):
    assembly_id = models.AutoField(primary_key=True)
    assembly_accession = models.CharField(max_length=16, blank=True, null=True)
    assembly_name = models.CharField(max_length=200)
    assembly_default = models.CharField(max_length=200)
    assembly_ucsc = models.CharField(max_length=16, blank=True, null=True)
    assembly_level = models.CharField(max_length=50)
    base_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'assembly'
        unique_together = (('assembly_accession', 'assembly_default', 'base_count'),)


class AssemblySequence(models.Model):
    assembly_sequence_id = models.AutoField(primary_key=True)
    assembly = models.ForeignKey(Assembly, models.DO_NOTHING)
    name = models.CharField(max_length=40)
    acc = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assembly_sequence'
        unique_together = (('assembly', 'name', 'acc'),)


class ComparaAnalysis(models.Model):
    compara_analysis_id = models.AutoField(primary_key=True)
    data_release_id = models.IntegerField()
    division = models.ForeignKey('Division', models.DO_NOTHING)
    method = models.CharField(max_length=50)
    set_name = models.CharField(max_length=128, blank=True, null=True)
    dbname = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'compara_analysis'
        unique_together = (('division', 'method', 'set_name', 'dbname'),)


class ComparaAnalysisEvent(models.Model):
    compara_analysis_event_id = models.AutoField(primary_key=True)
    compara_analysis = models.ForeignKey(ComparaAnalysis, models.DO_NOTHING)
    type = models.CharField(max_length=32)
    source = models.CharField(max_length=128, blank=True, null=True)
    creation_time = models.DateTimeField()
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compara_analysis_event'


class DataRelease(models.Model):
    data_release_id = models.AutoField(primary_key=True)
    ensembl_version = models.IntegerField()
    ensembl_genomes_version = models.IntegerField(blank=True, null=True)
    release_date = models.DateField()
    is_current = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_release'
        unique_together = (('ensembl_version', 'ensembl_genomes_version'),)


class DataReleaseDatabase(models.Model):
    data_release_database_id = models.AutoField(primary_key=True)
    data_release = models.ForeignKey(DataRelease, models.DO_NOTHING)
    dbname = models.CharField(max_length=64)
    type = models.CharField(max_length=8, blank=True, null=True)
    division = models.ForeignKey('Division', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_release_database'
        unique_together = (('data_release', 'dbname'),)


class DataReleaseDatabaseEvent(models.Model):
    data_release_database_event_id = models.AutoField(primary_key=True)
    data_release_database = models.ForeignKey(DataReleaseDatabase, models.DO_NOTHING)
    type = models.CharField(max_length=32)
    source = models.CharField(max_length=128, blank=True, null=True)
    creation_time = models.DateTimeField()
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_release_database_event'


class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    short_name = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = False
        db_table = 'division'


class Genome(models.Model):
    genome_id = models.AutoField(primary_key=True)
    data_release = models.ForeignKey(DataRelease, models.DO_NOTHING)
    assembly = models.ForeignKey(Assembly, models.DO_NOTHING)
    organism = models.ForeignKey('Organism', models.DO_NOTHING)
    genebuild = models.CharField(max_length=255)
    division = models.ForeignKey(Division, models.DO_NOTHING)
    has_pan_compara = models.IntegerField()
    has_variations = models.IntegerField()
    has_peptide_compara = models.IntegerField()
    has_genome_alignments = models.IntegerField()
    has_synteny = models.IntegerField()
    has_other_alignments = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'genome'
        unique_together = (('data_release', 'genome_id', 'division'),)


class GenomeAlignment(models.Model):
    genome_alignment_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.DO_NOTHING)
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    count = models.IntegerField()
    genome_database = models.ForeignKey('GenomeDatabase', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'genome_alignment'
        unique_together = (('genome', 'type', 'name', 'genome_database'),)


class GenomeAnnotation(models.Model):
    genome_annotation_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.DO_NOTHING)
    type = models.CharField(max_length=32)
    value = models.CharField(max_length=128)
    genome_database = models.ForeignKey('GenomeDatabase', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'genome_annotation'
        unique_together = (('genome', 'type', 'genome_database'),)


class GenomeComparaAnalysis(models.Model):
    genome_compara_analysis_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.DO_NOTHING)
    compara_analysis = models.ForeignKey(ComparaAnalysis, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'genome_compara_analysis'
        unique_together = (('genome', 'compara_analysis'),)


class GenomeDatabase(models.Model):
    genome_database_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.DO_NOTHING)
    dbname = models.CharField(max_length=64)
    species_id = models.IntegerField()
    type = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genome_database'
        unique_together = (('genome', 'dbname', 'species_id'),)


class GenomeEvent(models.Model):
    genome_event_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.DO_NOTHING)
    type = models.CharField(max_length=32)
    source = models.CharField(max_length=128, blank=True, null=True)
    creation_time = models.DateTimeField()
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genome_event'


class GenomeFeature(models.Model):
    genome_feature_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.DO_NOTHING)
    type = models.CharField(max_length=32)
    analysis = models.CharField(max_length=128)
    count = models.IntegerField()
    genome_database = models.ForeignKey(GenomeDatabase, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'genome_feature'
        unique_together = (('genome', 'type', 'analysis', 'genome_database'),)


class GenomeVariation(models.Model):
    genome_variation_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.DO_NOTHING)
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    count = models.IntegerField()
    genome_database = models.ForeignKey(GenomeDatabase, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'genome_variation'
        unique_together = (('genome', 'type', 'name', 'genome_database'),)


class Organism(models.Model):
    organism_id = models.AutoField(primary_key=True)
    taxonomy_id = models.IntegerField()
    reference = models.CharField(max_length=128, blank=True, null=True)
    species_taxonomy_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=128)
    url_name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    scientific_name = models.CharField(max_length=128)
    strain = models.CharField(max_length=128, blank=True, null=True)
    serotype = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organism'


class OrganismAlias(models.Model):
    organism_alias_id = models.AutoField(primary_key=True)
    organism = models.ForeignKey(Organism, models.DO_NOTHING)
    alias = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organism_alias'
        unique_together = (('organism', 'alias'),)


class OrganismPublication(models.Model):
    organism_publication_id = models.AutoField(primary_key=True)
    organism = models.ForeignKey(Organism, models.DO_NOTHING)
    publication = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organism_publication'
        unique_together = (('organism', 'publication'),)
