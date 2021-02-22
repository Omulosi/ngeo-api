from rest_framework import serializers
from django.contrib.gis.geos import fromstr
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from ...models import Incident


class IncidentSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Incident
        geo_field = "location"
        fields = "__all__"
