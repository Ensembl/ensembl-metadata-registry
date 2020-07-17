# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-07-15 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadata_registry', '0003_assembly_karyotype_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='genome_division',
            fields=[
                ('genome_division_id', models.AutoField(primary_key=True, serialize=False)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.Division')),
                ('genome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata_registry.Genome')),
            ],
        ),
    ]