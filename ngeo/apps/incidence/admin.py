from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Incident


class IncidentAdmin(OSMGeoAdmin):
    list_display = ("title", "date_reported", "location")
    search_fields = ("title",)
    filter_fields = ("title", "date_reported")


admin.site.register(Incident, IncidentAdmin)
