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

from django.db import models
from datarelease.models import DataRelease
from division.models import Division


# Create your models here.
class ComparaAnalysis(models.Model):
    MANY2ONE_RELATED = {'DATA_RELEASE': 'data_release_compara', 'DIVISION': 'division_compara'}
    ONE2MANY_RELATED = {'GENOME_COMPARA_ANALYSIS': 'genome_compara_analysis'}

    compara_analysis_id = models.AutoField(primary_key=True)
    genome_compara_analysis = models.ManyToManyField('genomeinfo.Genome', through='genomeinfo.GenomeComparaAnalysis',
                                                     related_name='genome_compara_analysis')
    method = models.CharField(max_length=50)
    set_name = models.CharField(max_length=128, blank=True, null=True)
    dbname = models.CharField(max_length=64)
    data_release = models.ForeignKey(DataRelease, models.DO_NOTHING, related_name=MANY2ONE_RELATED['DATA_RELEASE'])
    division = models.ForeignKey(Division, models.DO_NOTHING, related_name=MANY2ONE_RELATED['DIVISION'])

    class Meta:
        managed = False
        db_table = 'compara_analysis'
        unique_together = (('method', 'set_name', 'dbname'),)


class ComparaAnalysisEvent(models.Model):
    compara_analysis_event_id = models.AutoField(primary_key=True)
    compara_analysis = models.ForeignKey('ComparaAnalysis', models.DO_NOTHING)
    type = models.CharField(max_length=32)
    source = models.CharField(max_length=128, blank=True, null=True)
    creation_time = models.DateTimeField()
    details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compara_analysis_event'
