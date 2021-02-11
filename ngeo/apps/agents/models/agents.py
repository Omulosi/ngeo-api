from django.db import models

from ngeo.apps.field_officer.models import FieldOfficer
from ngeo.apps.shapefiles.models import IsioloProject

class Agent(models.Model):
    field_officer = models.ForeignKey(FieldOfficer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    rating = models.IntegerField(blank=True, null=True)
    id_number = models.IntegerField()
    phone_number = models.IntegerField()
    projects = models.ForeignKey(IsioloProject, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = 'agents'
