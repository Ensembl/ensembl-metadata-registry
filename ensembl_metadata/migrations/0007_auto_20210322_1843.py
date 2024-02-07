# Generated by Django 3.1.7 on 2021-03-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensembl_metadata', '0006_auto_20210317_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparaanalysisevent',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='genome',
            name='has_genome_alignments',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='genome',
            name='has_microarray',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='genome',
            name='has_other_alignments',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='genome',
            name='has_pan_compara',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='genome',
            name='has_peptide_compara',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='genome',
            name='has_synteny',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='genome',
            name='has_variation',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='genomeevent',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]