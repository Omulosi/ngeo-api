
from rest_framework import serializers
from ...models import FieldOfficer

class FieldOfficerSerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldOfficer
        fields = '__all__'