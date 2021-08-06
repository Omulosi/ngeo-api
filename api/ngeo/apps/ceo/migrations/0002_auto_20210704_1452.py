# Generated by Django 3.1.5 on 2021-07-04 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ceo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ceomodel',
            options={'verbose_name_plural': 'CEOs'},
        ),
        migrations.AlterField(
            model_name='ceomodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ceo', to=settings.AUTH_USER_MODEL),
        ),
    ]
