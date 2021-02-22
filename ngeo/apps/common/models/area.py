from django.db import models
from ngeo.apps.field_officer.models import FieldOfficer
from ngeo.apps.agents.models import Agent
from ngeo.apps.county_manager.models import CountyManager


class Area(models.Model):
    sub_location = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    sub_county = models.CharField(max_length=200, blank=True, null=True)
    county = models.CharField(max_length=200, blank=True, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, blank=True, null=True)
    field_officer = models.ForeignKey(FieldOfficer, on_delete=models.SET_NULL, blank=True, null=True)
    county_manager = models.ForeignKey(CountyManager, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "areas"
