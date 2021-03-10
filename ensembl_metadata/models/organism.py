from django.db import models
from ncbi_taxonomy.models import TaxonomyNode


class Organism(models.Model):
    organism_id = models.AutoField(primary_key=True)
    taxonomy_id = models.IntegerField()
    reference = models.CharField(max_length=128, blank=True, null=True)
    species_taxonomy_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=128)
    display_name = models.CharField(max_length=128)
    strain = models.CharField(max_length=128, blank=True, null=True)
    scientific_name = models.CharField(max_length=128, blank=True, null=True)
    url_name = models.CharField(max_length=128)
    group = models.ForeignKey('ensembl_metadata.OrganismGroup', on_delete=models.CASCADE,
                              related_name='organisms', blank=True,
                              null=True)

    class Meta:
        managed = True
        db_table = 'organism'

    def taxon(self):
        return TaxonomyNode.objects.get(taxon_id=self.taxonomy_id)


class OrganismAlias(models.Model):
    organism_alias_id = models.AutoField(primary_key=True)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE, related_name='aliases')
    alias = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'organism_alias'
        unique_together = (('organism', 'alias'),)


class OrganismGroup(models.Model):
    group_id = models.AutoField(primary_key=True, blank=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    label = models.CharField(max_length=255, blank=True, null=True)
    reference_organism = models.ForeignKey(Organism,
                                           null=True,
                                           on_delete=models.CASCADE,
                                           related_name='reference_groups')

    class Meta:
        managed = True
        db_table = 'group'

