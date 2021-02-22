from django.urls import path, re_path
from .views import (
    CountyList, 
    SubLocationList, 
    CountyName, 
    SubLocationName, 
    IsioloProjectDetail, 
    IsioloProjectList,
    IsioloKeyInstallationDetail,
    IsioloKeyInstallationList
)

urlpatterns = [
    path("counties", CountyList.as_view(), name="counties"),
    re_path("^counties/name/(?P<county_name>.+)/$", CountyName.as_view(), name="countyname"),
    path("sublocations", SubLocationList.as_view(), name="sublocations"),
    re_path("^sublocations/name/(?P<sublocation_name>.+)/$", SubLocationName.as_view(), name="sublocationname"),
    path("isiolo_projects", IsioloProjectList.as_view(), name="isiolo_projects"),
    path("isiolo_projects/<int:pk>", IsioloProjectDetail.as_view(), name="isiolo_project_detail"),
    path("isiolo_key_installations", IsioloKeyInstallationList.as_view(), name="isiolo_key_installations"),
]
