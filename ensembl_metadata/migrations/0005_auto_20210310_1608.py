# Generated by Django 3.1.6 on 2021-03-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensembl_metadata', '0004_auto_20210310_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='assemblysequence',
            name='chromosomal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='assemblysequence',
            name='length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assemblysequence',
            name='sequence_location',
            field=models.CharField(default='SO:0000738', max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='assemblysequence',
            unique_together={('assembly', 'name')},
        ),
        migrations.DeleteModel(
            name='AssemblyKaryotype',
        ),
    ]
