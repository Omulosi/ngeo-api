from rest_framework import generics
from ngeo.apps.agents.models import AgentReturn
from ..serializers import AgentReturnSerializer


class AgentReturnListCreate(generics.ListCreateAPIView):
    """
    API view to retrieve list of agents
    """
    serializer_class = AgentReturnSerializer
    queryset = AgentReturn.objects.all()


class AgentReturnDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve one agent
    """
    queryset = AgentReturn.objects.all()
    serializer_class = AgentReturnSerializer