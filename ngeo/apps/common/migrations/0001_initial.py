# Generated by Django 3.1.5 on 2021-02-18 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agents', '0005_auto_20210218_1434'),
        ('field_officer', '0004_auto_20210218_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_location', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('district', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_county', models.CharField(blank=True, max_length=200, null=True)),
                ('county', models.CharField(blank=True, max_length=200, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agents.agent')),
                ('field_officer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='field_officer.fieldofficer')),
            ],
            options={
                'verbose_name_plural': 'areas',
            },
        ),
    ]
