# Generated by Django 3.1.5 on 2021-06-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0015_auto_20210618_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='id_number',
            field=models.CharField(default='4f58190f-20b6-45f3-aa9c-2c7086be822a', max_length=200, unique=True),
        ),
    ]