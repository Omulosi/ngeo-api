# Generated by Django 3.1.5 on 2021-06-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20210615_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='latitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='longitude',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
