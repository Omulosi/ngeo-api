from django.db import models
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager
from ngeo.apps.agents.models import Agent
from ngeo.apps.field_officer.models import FieldOfficer


BUSINESS_INCUBATION = 1
AGRI_BUSINESS = 2
WATER_SANITATION = 3

THEME_CHOICES = (
    (BUSINESS_INCUBATION, 'BUSINESS INCUBATION'),
    (AGRI_BUSINESS, 'AGRI-BUSINESS'),
    (WATER_SANITATION, 'WATER-SANITATION'),
)


class Project(models.Model):
    name = models.CharField(max_length=200)
    theme = models.PositiveSmallIntegerField(choices=THEME_CHOICES, default=1)
    description = models.TextField(null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, blank=True, null=True, related_name='projects')
    field_officer = models.ForeignKey(FieldOfficer, on_delete=models.SET_NULL, blank=True, null=True, related_name='field_officer')
    location = gis_models.PointField(srid=4326, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"