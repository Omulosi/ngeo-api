# Generated by Django 3.1.5 on 2021-06-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0024_agent_approve_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='deny_approve_delete_message',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
