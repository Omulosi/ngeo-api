from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from ...models import Incidence

class IncidenceSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Incidence
        geo_field = "location"
        fields = '__all__'