
from rest_framework import serializers
from ...models import CountyManager

class CountyManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CountyManager
        fields = '__all__'