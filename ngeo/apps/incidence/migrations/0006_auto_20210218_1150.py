# Generated by Django 3.1.5 on 2021-02-18 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("incidence", "0005_auto_20210218_1130"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="incident",
            name="created",
        ),
        migrations.RemoveField(
            model_name="incident",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="incident",
            name="updated",
        ),
        migrations.RemoveField(
            model_name="incident",
            name="uuid",
        ),
        migrations.AddField(
            model_name="incident",
            name="id",
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
            preserve_default=False,
        ),
    ]
