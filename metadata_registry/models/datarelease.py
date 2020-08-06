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
    label = models.CharField(max_length=64)
    version = models.IntegerField()
    release_date = models.DateField()
    is_current = models.IntegerField(blank=True, null=True)
    site_id = models.ForeignKey('metadata_registry.EnsemblSite', on_delete=models.CASCADE,
                              related_name='site_id_release', blank=True,
                              null=True)

    class Meta:
        managed = True
        db_table = 'ensembl_release'


class EnsemblSite(models.Model):
    site_id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=64)
    uri = models.CharField(max_length=64)

    class Meta:
        managed = True
        db_table = 'ensembl_site'
