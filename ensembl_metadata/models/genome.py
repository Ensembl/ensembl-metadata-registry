from django.db import models
from ensembl_metadata.models.assembly import Assembly
from ensembl_metadata.models.release import Release
from ncbi_taxonomy.models import TaxonomyNode
import uuid


class Organism(models.Model):
    organism_id = models.AutoField(primary_key=True)
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
        db_table = 'organism'


class OrganismGroup(models.Model):
    class GroupType(models.TextChoices):
        BREEDS = 'breeds'
        CULTIVARS = 'cultivars'
        DIVISION = 'division'
        POPULATIONS = 'populations'
        STRAINS = 'strains'

    organism_group_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32, choices=GroupType.choices)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'organism_group'
        unique_together = (('type', 'name'),)


class OrganismGroupMember(models.Model):
    organism_group_member_id = models.AutoField(primary_key=True)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE,
                                 related_name='members')
    organism_group = models.ForeignKey(OrganismGroup, on_delete=models.CASCADE,
                                       related_name='members')
    is_reference = models.BooleanField(default=False)

    class Meta:
        db_table = 'organism_group_member'
        unique_together = (('organism', 'organism_group'),)


class Genome(models.Model):
    genome_id = models.AutoField(primary_key=True)
    genome_uuid = models.CharField(max_length=128, default=uuid.uuid1, unique=True)
    assembly = models.ForeignKey(Assembly, models.CASCADE, related_name='genomes')
    organism = models.ForeignKey(Organism, models.CASCADE, related_name='genomes')

    def releases(self):
        return GenomeRelease.objects.filter(genome_id=self.genome_id)

    class Meta:
        db_table = 'genome'


class DatasetSource(models.Model):
    class SourceType(models.TextChoices):
        CORE = 'core'
        CDNA = 'cdna'
        DATAFILE = 'datafile'
        OTHERFEATURES = 'otherfeatures'
        RNASEQ = 'rnaseq'
        COMPARA = 'compara'
        FUNCGEN = 'funcgen'
        VARIATION = 'variation'

    dataset_source_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32, choices=SourceType.choices)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'dataset_source'


class DatasetType(models.Model):
    class DatasetTopic(models.TextChoices):
        ASSEMBLY = 'assembly'
        GENESET = 'geneset'
        ASSEMBLY_ANNOTATION = 'assembly_annotation'
        GENESET_ANNOTATION = 'geneset_annotation'
        COMPARATIVE = 'comparative'
        REGULATION = 'regulation'
        VARIATION = 'variation'

    dataset_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    label = models.CharField(max_length=32)
    topic = models.CharField(max_length=32, choices=DatasetTopic.choices)
    description = models.CharField(max_length=255)
    details_uri = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'dataset_type'


class Dataset(models.Model):
    dataset_id = models.AutoField(primary_key=True)
    dataset_uuid = models.CharField(max_length=128, default=uuid.uuid1, unique=True)
    dataset_type = models.ForeignKey(DatasetType, on_delete=models.CASCADE,
                                     related_name='datasets')
    dataset_source = models.ForeignKey(DatasetSource, on_delete=models.CASCADE,
                                       related_name='datasets')
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=128, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def attributes(self):
        return DatasetStatistic.objects.filter(dataset_id=self.dataset_id)

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


class GenomeDataset(models.Model):
    genome_dataset_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='datasets')
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE,
                                related_name='genomes')
    release = models.ForeignKey(Release, on_delete=models.CASCADE,
                                related_name='genome_datasets')

    class Meta:
        db_table = 'genome_dataset'


class GenomeRelease(models.Model):
    genome_release_id = models.AutoField(primary_key=True)
    genome = models.ForeignKey(Genome, on_delete=models.CASCADE,
                               related_name='releases')
    release = models.ForeignKey(Release, on_delete=models.CASCADE,
                                related_name='releases')

    class Meta:
        db_table = 'genome_release'
