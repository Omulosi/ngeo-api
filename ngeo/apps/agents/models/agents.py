from django.db import models

from ngeo.apps.field_officer.models import FieldOfficer
from ngeo.apps.shapefiles.models import IsioloProject


class Agent(models.Model):

    PERMANENT = 1
    TEMPORARY = 2
    CASUAL = 3

    TERMS_CHOICES = ((PERMANENT, "PERMANENT"), (TEMPORARY, "TEMPORARY"), (CASUAL, "CASUAL"))

    field_officer = models.ForeignKey(FieldOfficer, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    id_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    terms = models.PositiveSmallIntegerField(choices=TERMS_CHOICES, blank=True, null=True, default=3)

    class Meta:
        verbose_name_plural = "agents"
