from django.db import models


class TaxonomyNode(models.Model):
    taxon_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    rank = models.CharField(max_length=32)
    genbank_hidden_flag = models.IntegerField()
    left_index = models.IntegerField()
    right_index = models.IntegerField()
    root_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'ncbi_taxa_node'
        verbose_name = 'Taxon'

    def __str__(self):
        return str(self.taxon_id)

    def names(self):
        name_classes = [
            'common name',
            'equivalent name',
            'genbank common name',
            'genbank synonym',
            'synonym'
        ]
        return TaxonomyName.objects.filter(taxon_id=self, name_class__in=name_classes)


class TaxonomyName(models.Model):
    name_id = models.AutoField(primary_key=True)
    taxon = models.ForeignKey(TaxonomyNode, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    name_class = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'ncbi_taxa_name'
        verbose_name = 'Taxon name'
        unique_together = (('taxon', 'name', 'name_class'),)

    def __str__(self):
        return '{}: {} = {}'.format(self.taxon_id, self.name_class, self.name)
