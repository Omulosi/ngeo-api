# Generated by Django 3.1.5 on 2021-05-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20210503_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
