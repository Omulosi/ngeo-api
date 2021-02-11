from rest_framework import generics
from ..serializers import ProjectSerializer
from ...models import Project

class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectDetail(generics.RetrieveDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()