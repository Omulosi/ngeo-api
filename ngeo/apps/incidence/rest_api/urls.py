from django.urls import path
from .views import IncidenceList, IncidenceDetail


urlpatterns = [
    path("incidences", IncidenceList.as_view(), name="incidences")
]
