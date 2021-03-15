from django.db import models
from ensembl_metadata.models.assembly import Assembly
from ensembl_metadata.models.release import Release
from ncbi_taxonomy.models import TaxonomyNode
import uuid


class Genome(models.Model):
    genome_id = models.AutoField(primary_key=True)
    genome_uuid = models.CharField(max_length=128, default=uuid.uuid1, unique=True)
    assembly = models.ForeignKey(Assembly, models.CASCADE, related_name='genomes')
    taxonomy_id = models.IntegerField()
    species_taxonomy_id = models.IntegerField(null=True)
    ensembl_name = models.CharField(unique=True, max_length=128)
    url_name = models.CharField(max_length=128)
    display_name = models.CharField(max_length=128)
    scientific_name = models.CharField(max_length=128, blank=True, null=True)
    strain = models.CharField(max_length=128, blank=True, null=True)

    def taxon(self):
        return TaxonomyNode.objects.get(taxon_id=self.taxonomy_id)

    class Meta:
        db_table = 'genome'


class Bundle(models.Model):
    bundle_id = models.AutoField(primary_key=True, blank=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'bundle'
        unique_together = (('type', 'name'),)


class GenomeBundle(models.Model):
    genome_bundle_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='genome_bundles')
    bundle = models.ForeignKey(Bundle, on_delete=models.CASCADE,
                               related_name='genome_bundles')
    is_reference = models.BooleanField(default=False)
    release_id = models.ForeignKey(Release, on_delete=models.CASCADE,
                                   related_name='genome_bundles')

    class Meta:
        db_table = 'genome_bundle'
        unique_together = (('genome', 'bundle'),)


class DatasetDatabase(models.Model):
    class DatabaseType(models.TextChoices):
        CORE = 'core'
        CDNA = 'cdna'
        OTHERFEATURES = 'otherfeatures'
        RNASEQ = 'rnaseq'
        COMPARA = 'compara'
        FUNCGEN = 'funcgen'
        VARIATION = 'variation'

    dataset_database_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32, choices=DatabaseType.choices)
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        db_table = 'dataset_database'


class Dataset(models.Model):
    class DatasetType(models.TextChoices):
        ASSEMBLY = 'assembly'
        CROSS_REFERENCES = 'xrefs'
        DNA_ALIGNMENTS = 'dna_alignments'
        GENESET = 'geneset'
        GENE_FAMILIES = 'gene_families'
        GENE_TREES = 'gene_trees'
        GENOME_ALIGNMENTS = 'genome_alignments'
        GO_TERMS = 'go_terms'
        HOMOLOGIES = 'homologies'
        MICROARRAYS = 'microarrays'
        PHENOTYPES = 'phenotypes'
        PROTEIN_ALIGNMENTS = 'protein_alignments'
        PROTEIN_FEATURES = 'protein_features'
        REPEAT_FEATURES = 'repeat_features'
        RNASEQ_ALIGNMENTS = 'rnaseq_alignments'
        SYNTENIES = 'syntenies'
        VARIANTS = 'variants'

    dataset_id = models.AutoField(primary_key=True)
    dataset_uuid = models.CharField(max_length=128, default=uuid.uuid1, unique=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='datasets')
    dataset_database = models.ForeignKey(DatasetDatabase, on_delete=models.CASCADE,
                                         related_name='datasets')
    type = models.CharField(max_length=32, choices=DatasetType.choices)
    name = models.CharField(max_length=128, null=True)
    version = models.CharField(max_length=128, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def attributes(self):
        return DatasetStatistic.objects.filter(dataset_id=self.dataset_id)

    def releases(self):
        return DatasetRelease.objects.filter(dataset_id=self.dataset_id)

    class Meta:
        db_table = 'dataset'


class DatasetStatistic(models.Model):
    dataset_statistic_id = models.AutoField(primary_key=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE,
                                related_name='statistics')
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    class Meta:
        db_table = 'dataset_statistic'
        unique_together = (('dataset', 'type', 'name'),)


class DatasetRelease(models.Model):
    dataset_release_id = models.AutoField(primary_key=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE,
                                related_name='dataset_releases')
    release = models.ForeignKey(Release, on_delete=models.CASCADE,
                                related_name='dataset_releases')

    class Meta:
        db_table = 'dataset_release'
