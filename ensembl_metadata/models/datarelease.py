from django.db import models


class Site(models.Model):
    site_id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=64)
    uri = models.CharField(max_length=64)

    class Meta:
        db_table = 'ensembl_site'


class DataRelease(models.Model):
    data_release_id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=64)
    version = models.IntegerField()
    release_date = models.DateField()
    is_current = models.IntegerField(blank=True, null=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE,
                             blank=True, null=True,
                             related_name='data_releases')

    class Meta:
        db_table = 'ensembl_release'
        unique_together = (('version', 'site'),)
