# Generated by Django 3.1.5 on 2021-06-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0014_auto_20210616_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='id_number',
            field=models.CharField(default='8236bb37-636b-4898-b37e-0ded93381e40', max_length=200, unique=True),
        ),
    ]
