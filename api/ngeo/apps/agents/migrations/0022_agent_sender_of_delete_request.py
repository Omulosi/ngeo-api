# Generated by Django 3.1.5 on 2021-06-24 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('field_officer', '0001_initial'),
        ('agents', '0021_agent_approve_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='sender_of_delete_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delete_sender', to='field_officer.fieldofficer'),
        ),
    ]