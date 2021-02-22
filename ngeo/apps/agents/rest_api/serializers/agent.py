
from rest_framework import serializers
from ...models import Agent, AgentReturn

class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = '__all__'

class AgentReturnSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgentReturn
        fields = '__all__'