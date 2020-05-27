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


class Organism(models.Model):

    ONE2MANY_RELATED = {'ORGANISM_ALIAS': 'organism_alias', 'ORGANISM_PUBLICAION': 'organism_publication'}

    organism_id = models.AutoField(primary_key=True)
    taxonomy_id = models.IntegerField()
    reference = models.CharField(max_length=128)
    species_taxonomy_id = models.IntegerField()
    name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    strain = models.CharField(max_length=128, blank=True, null=True)
    serotype = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    scientific_name = models.CharField(max_length=128, blank=True, null=True)
    url_name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'organism'


class OrganismAlias(models.Model):
    organism_alias_id = models.AutoField(primary_key=True)
    organism = models.ForeignKey(Organism, models.DO_NOTHING, related_name=Organism.ONE2MANY_RELATED['ORGANISM_ALIAS'])
    alias = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organism_alias'
        unique_together = (('organism', 'alias'),)


class OrganismPublication(models.Model):
    organism_publication_id = models.AutoField(primary_key=True)
    organism = models.ForeignKey(Organism, models.DO_NOTHING,
                                 related_name=Organism.ONE2MANY_RELATED['ORGANISM_PUBLICAION'])
    publication = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organism_publication'
        unique_together = (('organism', 'publication'),)
