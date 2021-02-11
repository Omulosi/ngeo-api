"""County view."""

from rest_framework import generics
from ngeo.apps.shapefiles.models import SubLocation
from ngeo.apps.shapefiles.rest_api.serializers import SublocationSerializer

from .filters import SublocationFilter

class SubLocationList(generics.ListAPIView):
    """
    API view to retrieve list of counties
    """
    queryset = SubLocation.objects.all()
    serializer_class = SublocationSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SublocationFilter
    # filterset_fields = ('locname', 'divname')
    search_fields = ('locname', )


class SubLocationDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve one county
    """
    queryset = SubLocation.objects.all()
    serializer_class = SublocationSerializer
    filterset_fields = ('locname', 'divname', 'distname', 'provname', 'sub_name',)

class SubLocationName(generics.ListAPIView):
    """
    API view to retrieve list of counties
    """
    serializer_class = SublocationSerializer

    def get_queryset(self):
        queryset = SubLocation.objects.all()
        sublocation_name = self.kwargs.get('sublocation_name', None)
        if sublocation_name is not None:
            queryset = queryset.filter(sub_name__iexact=sublocation_name)
        return queryset
