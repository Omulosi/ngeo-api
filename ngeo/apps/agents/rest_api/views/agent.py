from rest_framework import generics
from ...models import Agent
from ..serializers import AgentSerializer


class AgentListCreate(generics.ListCreateAPIView):
    """
    API view to retrieve list of agents
    """
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()


class AgentDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve one agent
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer