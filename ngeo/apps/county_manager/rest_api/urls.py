from django.urls import path
from .views import CountyManagerList, CountyManagerDetail


urlpatterns = [
    path("county_managers", CountyManagerList.as_view(), name="county_manager_list"),
    path("county_managers/<int:pk>", CountyManagerDetail.as_view(), name="county_manager_detail")
]
