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

from django.db import models
from metadata_registry.models.datarelease import DataRelease
from metadata_registry.models.assembly import Assembly
from metadata_registry.models.organism import Organism
from metadata_registry.models.compara import ComparaAnalysis
from metadata_registry.models.division import Division
import uuid


# Create your models here.
class Genome(models.Model):

    MANY2ONE_RELATED = {'ASSEMBLY': 'assembly', 'ORGANISM': 'organism',
                        'DIVISION': 'division'}
    ONE2MANY_RELATED = {'GENOME_ALIGNMENT': 'genome_alignment', 'GENOME_ANNOTATION': 'genome_annotation',
                        'GENOME_DATABASE': 'genome_database', 'GENOME_EVENT': 'genome_event',
                        'GENOME_FEATURE': 'genome_feature', 'GENOME_VARIATION': 'genome_variation',
                        'GENOME_COMPARA_ANALYSIS': 'genome_compara_analysis'}

    genome_id = models.IntegerField(primary_key=True)
    genome_uuid = models.CharField(max_length=128, default=uuid.uuid1, unique=True)
    assembly = models.ForeignKey(Assembly, models.CASCADE, related_name=MANY2ONE_RELATED['ASSEMBLY'])
    organism = models.ForeignKey(Organism, models.CASCADE, related_name=MANY2ONE_RELATED['ORGANISM'])
    genebuild = models.CharField(max_length=64)
    has_pan_compara = models.IntegerField()
    has_variation = models.IntegerField()
    has_microarray = models.IntegerField()
    has_peptide_compara = models.IntegerField()
    has_genome_alignments = models.IntegerField()
    has_synteny = models.IntegerField()
    has_other_alignments = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'genome'

class GenomeDatabase(models.Model):

    ONE2MANY_RELATED = {'GENOME_ALIGNMENT': 'genome_alignment', 'GENOME_ANNOTATION': 'genome_annotation',
                        'GENOME_FEATURE': 'genome_feature', 'GENOME_VARIATION': 'genome_variation'}
    genome_database_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.CASCADE, related_name=Genome.ONE2MANY_RELATED['GENOME_DATABASE'])
    dbname = models.CharField(max_length=64)
    species_id = models.IntegerField()
    type = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'genome_database'
        unique_together = (('dbname', 'species_id'), ('genome', 'dbname'),)


class GenomeAlignment(models.Model):
    genome_alignment_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.CASCADE, related_name=Genome.ONE2MANY_RELATED['GENOME_ALIGNMENT'])
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    count = models.IntegerField()
    genome_database = models.ForeignKey(GenomeDatabase, models.CASCADE,
                                        related_name=GenomeDatabase.ONE2MANY_RELATED['GENOME_ALIGNMENT'])

    class Meta:
        managed = True
        db_table = 'genome_alignment'
        unique_together = (('genome', 'type', 'name', 'genome_database'),)


class GenomeAnnotation(models.Model):
    genome_annotation_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.CASCADE, related_name=Genome.ONE2MANY_RELATED['GENOME_ANNOTATION'])
    type = models.CharField(max_length=32)
    value = models.CharField(max_length=128)
    genome_database = models.ForeignKey(GenomeDatabase, models.CASCADE,
                                        related_name=GenomeDatabase.ONE2MANY_RELATED['GENOME_ANNOTATION'])

    class Meta:
        managed = True
        db_table = 'genome_annotation'
        unique_together = (('genome', 'type', 'genome_database'),)


class GenomeComparaAnalysis(models.Model):
    genome_compara_analysis_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.CASCADE)
    compara_analysis = models.ForeignKey(ComparaAnalysis, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'genome_compara_analysis'
        unique_together = (('genome', 'compara_analysis'),)


class GenomeEvent(models.Model):
    genome_event_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.CASCADE, related_name=Genome.ONE2MANY_RELATED['GENOME_EVENT'])
    type = models.CharField(max_length=32)
    source = models.CharField(max_length=128, blank=True, null=True)
    creation_time = models.DateTimeField()
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'genome_event'


class GenomeFeature(models.Model):
    genome_feature_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.CASCADE, related_name=Genome.ONE2MANY_RELATED['GENOME_FEATURE'])
    type = models.CharField(max_length=32)
    analysis = models.CharField(max_length=128)
    count = models.IntegerField()
    genome_database = models.ForeignKey(GenomeDatabase, models.CASCADE,
                                        related_name=GenomeDatabase.ONE2MANY_RELATED['GENOME_FEATURE'])

    class Meta:
        managed = True
        db_table = 'genome_feature'
        unique_together = (('genome', 'type', 'analysis', 'genome_database'),)


class GenomeVariation(models.Model):
    genome_variation_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, models.CASCADE, related_name=Genome.ONE2MANY_RELATED['GENOME_VARIATION'])
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    count = models.IntegerField()
    genome_database = models.ForeignKey(GenomeDatabase, models.CASCADE,
                                        related_name=GenomeDatabase.ONE2MANY_RELATED['GENOME_VARIATION'])

    class Meta:
        managed = True
        db_table = 'genome_variation'
        unique_together = (('genome', 'type', 'name', 'genome_database'),)
        
class GenomeRelease(models.Model):
    genome_release_id = models.AutoField(primary_key=True)
    genome_uuid = models.ForeignKey('metadata_registry.Genome',on_delete=models.CASCADE)
    division = models.ForeignKey('metadata_registry.Division',on_delete=models.CASCADE)
    data_release = models.ForeignKey('metadata_registry.DataRelease',on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'genome_release'

class GenomeDivision(models.Model):
    genome_division_id = models.AutoField(primary_key=True)
    division = models.ForeignKey('metadata_registry.Division',on_delete=models.CASCADE)
    genome = models.ForeignKey('metadata_registry.Genome',on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'genome_division'