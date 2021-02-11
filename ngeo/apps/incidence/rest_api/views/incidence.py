from rest_framework import generics
from ..serializers import IncidenceSerializer
from ...models import Incidence

class IncidenceList(generics.ListCreateAPIView):
    serializer_class = IncidenceSerializer
    queryset = Incidence.objects.all()

class IncidenceDetail(generics.RetrieveDestroyAPIView):
    serializer_class = IncidenceSerializer
    queryset = Incidence.objects.all()