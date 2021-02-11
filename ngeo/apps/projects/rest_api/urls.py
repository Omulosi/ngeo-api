from django.urls import path
from .views import ProjectDetail, ProjectList


urlpatterns = [
    path("projects", ProjectList.as_view(), name="projects")
]
