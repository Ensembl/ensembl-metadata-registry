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


class Assembly(models.Model):
  
    ONE2MANY_RELATED = {'ASSEMBLY_SEQEUNCE': 'assembly_sequence'}

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
    assembly = models.ForeignKey(Assembly, models.DO_NOTHING,
                                 related_name=Assembly.ONE2MANY_RELATED['ASSEMBLY_SEQEUNCE'])

    name = models.CharField(max_length=40)
    acc = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'assembly_sequence'
        unique_together = (('assembly', 'name', 'acc'),)

