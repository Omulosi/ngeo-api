from rest_framework import generics
from ...models import FieldOfficer
from ..serializers import FieldOfficerSerializer


class FieldOfficerList(generics.ListAPIView):
    """
    API view to retrieve list of agents
    """
    serializer_class = FieldOfficerSerializer
    queryset = FieldOfficer.objects.all()


class FieldOfficerDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve one agent
    """
    serializer_class = FieldOfficerSerializer
    queryset = FieldOfficer.objects.all()