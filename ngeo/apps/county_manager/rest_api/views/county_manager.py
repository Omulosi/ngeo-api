from rest_framework import generics
from ...models import CountyManager
from ..serializers import CountyManagerSerializer


class CountyManagerList(generics.ListAPIView):
    """
    API view to retrieve list of county managers
    """
    serializer_class = CountyManagerSerializer
    queryset = CountyManager.objects.all()


class CountyManagerDetail(generics.RetrieveDestroyAPIView):
    """
    API view to retrieve one county manager
    """
    serializer_class = CountyManagerSerializer
    queryset = CountyManager.objects.all()