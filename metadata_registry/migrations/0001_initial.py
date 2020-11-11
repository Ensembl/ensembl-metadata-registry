# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-08-11 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('assembly_id', models.AutoField(primary_key=True, serialize=False)),
                ('assembly_accession', models.CharField(blank=True, max_length=16, null=True, unique=True)),
                ('assembly_name', models.CharField(max_length=200)),
                ('assembly_default', models.CharField(max_length=200)),
                ('assembly_ucsc', models.CharField(blank=True, max_length=16, null=True)),
                ('assembly_level', models.CharField(max_length=50)),
                ('base_count', models.BigIntegerField()),
            ],
            options={
                'db_table': 'assembly',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AssemblyKaryotype',
            fields=[
                ('assembly_karyotype_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(max_length=40)),
                ('region_start', models.IntegerField()),
                ('region_end', models.IntegerField()),
                ('band', models.CharField(max_length=50)),
                ('strain', models.CharField(max_length=50)),
                ('assembly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assembly_karyotype', to='metadata_registry.Assembly')),
            ],
            options={
                'db_table': 'assembly_karyotype',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AssemblySequence',
            fields=[
                ('assembly_sequence_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('acc', models.CharField(blank=True, max_length=24, null=True)),
                ('assembly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assembly_sequence', to='metadata_registry.Assembly')),
            ],
            options={
                'db_table': 'assembly_sequence',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ComparaAnalysis',
            fields=[
                ('compara_analysis_id', models.AutoField(primary_key=True, serialize=False)),
                ('method', models.CharField(max_length=50)),
                ('set_name', models.CharField(blank=True, max_length=128, null=True)),
                ('dbname', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'compara_analysis',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ComparaAnalysisEvent',
            fields=[
                ('compara_analysis_event_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=32)),
                ('source', models.CharField(blank=True, max_length=128, null=True)),
                ('creation_time', models.DateTimeField()),
                ('details', models.TextField(blank=True, null=True)),
                ('compara_analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.ComparaAnalysis')),
            ],
            options={
                'db_table': 'compara_analysis_event',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DataRelease',
            fields=[
                ('data_release_id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=64)),
                ('version', models.IntegerField()),
                ('release_date', models.DateField()),
                ('is_current', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ensembl_release',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('division_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('short_name', models.CharField(max_length=8, unique=True)),
            ],
            options={
                'db_table': 'division',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EnsemblSite',
            fields=[
                ('site_id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=64)),
                ('uri', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'ensembl_site',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Genome',
            fields=[
                ('genome_id', models.IntegerField(primary_key=True, serialize=False)),
                ('genome_uuid', models.CharField(default=uuid.uuid1, max_length=128, unique=True)),
                ('genebuild', models.CharField(max_length=64)),
                ('has_pan_compara', models.IntegerField()),
                ('has_variation', models.IntegerField()),
                ('has_microarray', models.IntegerField()),
                ('has_peptide_compara', models.IntegerField()),
                ('has_genome_alignments', models.IntegerField()),
                ('has_synteny', models.IntegerField()),
                ('has_other_alignments', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('assembly', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assembly', to='metadata_registry.Assembly')),
            ],
            options={
                'db_table': 'genome',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenomeAlignment',
            fields=[
                ('genome_alignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_alignment', to='metadata_registry.Genome')),
            ],
            options={
                'db_table': 'genome_alignment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenomeAnnotation',
            fields=[
                ('genome_annotation_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=32)),
                ('value', models.CharField(max_length=128)),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_annotation', to='metadata_registry.Genome')),
            ],
            options={
                'db_table': 'genome_annotation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenomeComparaAnalysis',
            fields=[
                ('genome_compara_analysis_id', models.AutoField(primary_key=True, serialize=False)),
                ('compara_analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.ComparaAnalysis')),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.Genome')),
            ],
            options={
                'db_table': 'genome_compara_analysis',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenomeDatabase',
            fields=[
                ('genome_database_id', models.AutoField(primary_key=True, serialize=False)),
                ('dbname', models.CharField(max_length=64)),
                ('species_id', models.IntegerField()),
                ('type', models.CharField(blank=True, max_length=13, null=True)),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_database', to='metadata_registry.Genome')),
            ],
            options={
                'db_table': 'genome_database',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenomeDivision',
            fields=[
                ('genome_division_id', models.AutoField(primary_key=True, serialize=False)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.Division')),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.Genome')),
            ],
            options={
                'db_table': 'genome_division',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenomeEvent',
            fields=[
                ('genome_event_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=32)),
                ('source', models.CharField(blank=True, max_length=128, null=True)),
                ('creation_time', models.DateTimeField()),
                ('details', models.TextField(blank=True, null=True)),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_event', to='metadata_registry.Genome')),
            ],
            options={
                'db_table': 'genome_event',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenomeFeature',
            fields=[
                ('genome_feature_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=32)),
                ('analysis', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_feature', to='metadata_registry.Genome')),
                ('genome_database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_feature', to='metadata_registry.GenomeDatabase')),
            ],
            options={
                'db_table': 'genome_feature',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenomeRelease',
            fields=[
                ('genome_release_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.DataRelease')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.Division')),
                ('genome_uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.Genome', to_field='genome_uuid')),
            ],
            options={
                'db_table': 'genome_release',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GenomeVariation',
            fields=[
                ('genome_variation_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_variation', to='metadata_registry.Genome')),
                ('genome_database', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_variation', to='metadata_registry.GenomeDatabase')),
            ],
            options={
                'db_table': 'genome_variation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('organism_id', models.AutoField(primary_key=True, serialize=False)),
                ('taxonomy_id', models.IntegerField()),
                ('reference', models.CharField(blank=True, max_length=128, null=True)),
                ('species_taxonomy_id', models.IntegerField()),
                ('name', models.CharField(max_length=128)),
                ('display_name', models.CharField(max_length=128)),
                ('strain', models.CharField(blank=True, max_length=128, null=True)),
                ('serotype', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('scientific_name', models.CharField(blank=True, max_length=128, null=True)),
                ('url_name', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'organism',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrganismAlias',
            fields=[
                ('organism_alias_id', models.AutoField(primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, max_length=255, null=True)),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organism_alias', to='metadata_registry.Organism')),
            ],
            options={
                'db_table': 'organism_alias',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrganismGroup',
            fields=[
                ('group_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_organism', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reference_groups', to='metadata_registry.Organism')),
            ],
            options={
                'db_table': 'group',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='OrganismPublication',
            fields=[
                ('organism_publication_id', models.AutoField(primary_key=True, serialize=False)),
                ('publication', models.CharField(blank=True, max_length=64, null=True)),
                ('organism', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organism_publication', to='metadata_registry.Organism')),
            ],
            options={
                'db_table': 'organism_publication',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='organism',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_organisms', to='metadata_registry.OrganismGroup'),
        ),
        migrations.AddField(
            model_name='genomeannotation',
            name='genome_database',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_annotation', to='metadata_registry.GenomeDatabase'),
        ),
        migrations.AddField(
            model_name='genomealignment',
            name='genome_database',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genome_alignment', to='metadata_registry.GenomeDatabase'),
        ),
        migrations.AddField(
            model_name='genome',
            name='organism',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organism', to='metadata_registry.Organism'),
        ),
        migrations.AddField(
            model_name='datarelease',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='site_id_release', to='metadata_registry.EnsemblSite'),
        ),
        migrations.AddField(
            model_name='comparaanalysis',
            name='data_release',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_release_compara', to='metadata_registry.DataRelease'),
        ),
        migrations.AddField(
            model_name='comparaanalysis',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='division_compara', to='metadata_registry.Division'),
        ),
        migrations.AddField(
            model_name='comparaanalysis',
            name='genome_compara_analysis',
            field=models.ManyToManyField(related_name='genome_compara_analysis', through='metadata_registry.GenomeComparaAnalysis', to='metadata_registry.Genome'),
        ),
        migrations.AlterUniqueTogether(
            name='assembly',
            unique_together=set([('assembly_accession', 'assembly_default', 'base_count')]),
        ),
        migrations.AlterUniqueTogether(
            name='organismpublication',
            unique_together=set([('organism', 'publication')]),
        ),
        migrations.AlterUniqueTogether(
            name='organismalias',
            unique_together=set([('organism', 'alias')]),
        ),
        migrations.AlterUniqueTogether(
            name='genomevariation',
            unique_together=set([('genome', 'type', 'name', 'genome_database')]),
        ),
        migrations.AlterUniqueTogether(
            name='genomefeature',
            unique_together=set([('genome', 'type', 'analysis', 'genome_database')]),
        ),
        migrations.AlterUniqueTogether(
            name='genomedatabase',
            unique_together=set([('dbname', 'species_id', 'genome')]),
        ),
        migrations.AlterUniqueTogether(
            name='genomecomparaanalysis',
            unique_together=set([('genome', 'compara_analysis')]),
        ),
        migrations.AlterUniqueTogether(
            name='genomeannotation',
            unique_together=set([('genome', 'type', 'genome_database')]),
        ),
        migrations.AlterUniqueTogether(
            name='genomealignment',
            unique_together=set([('genome', 'type', 'name', 'genome_database')]),
        ),
        migrations.AlterUniqueTogether(
            name='comparaanalysis',
            unique_together=set([('division','method', 'set_name', 'dbname')]),
        ),
        migrations.AlterUniqueTogether(
            name='assemblysequence',
            unique_together=set([('assembly', 'name', 'acc')]),
        ),
    ]
