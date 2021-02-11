from django.contrib import admin
from .models import FieldOfficer


@admin.register(FieldOfficer)
class FieldOfficerAdmin(admin.ModelAdmin):
    pass
