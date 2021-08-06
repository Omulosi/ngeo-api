# Generated by Django 3.1.5 on 2021-06-18 15:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0018_auto_20210618_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='id_number',
            field=models.CharField(default=uuid.uuid4, max_length=200, unique=True),
        ),
    ]
