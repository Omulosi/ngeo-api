from rest_framework import generics
from ..serializers import IncidentSerializer
from ...models import Incident
from .filters import IncidentFilter


class IncidentList(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    filterset_class = IncidentFilter
    search_fields = ("title",)


class IncidentDetail(generics.RetrieveAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
