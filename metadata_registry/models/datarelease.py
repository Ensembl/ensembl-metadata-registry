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


# Create your models here.
class DataRelease(models.Model):
    data_release_id = models.AutoField(primary_key=True)
    ensembl_version = models.IntegerField()
    ensembl_genomes_version = models.IntegerField(blank=True, null=True)
    release_date = models.DateField()
    is_current = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_release'
        unique_together = (('ensembl_version', 'ensembl_genomes_version'),)


class DataReleaseDatabase(models.Model):
    data_release_database_id = models.AutoField(primary_key=True)
    data_release = models.ForeignKey(DataRelease, models.DO_NOTHING)
    dbname = models.CharField(max_length=64)
    type = models.CharField(max_length=5, blank=True, null=True)
    division = models.ForeignKey('Division', models.DO_NOTHING)

    class Meta:
        managed = True
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
        managed = True
        db_table = 'data_release_database_event'
