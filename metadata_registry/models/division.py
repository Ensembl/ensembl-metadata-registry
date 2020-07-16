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
class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    short_name = models.CharField(unique=True, max_length=8)

    class Meta:
        managed = True
        db_table = 'division'

class genome_division(models.Model):
    genome_division_id = models.AutoField(primary_key=True)
    division = models.ForeignKey('metadata_registry.Division',on_delete=models.CASCADE)
    genome = models.ForeignKey('metadata_registry.Genome',on_delete=models.CASCADE)