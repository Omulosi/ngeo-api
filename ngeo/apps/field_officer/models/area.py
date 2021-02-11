from django.db import models
from .field_officer import FieldOfficer

class Area(models.Model):
    sub_location = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    sub_county = models.CharField(max_length=200, blank=True, null=True)
    county = models.CharField(max_length=200, blank=True, null=True)
    field_officer = models.ForeignKey(FieldOfficer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "areas"