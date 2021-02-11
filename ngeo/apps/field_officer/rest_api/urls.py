from django.urls import path
from .views import FieldOfficerList, FieldOfficerDetail


urlpatterns = [
    path("field_officers", FieldOfficerList.as_view(), name="field_officers")
]
