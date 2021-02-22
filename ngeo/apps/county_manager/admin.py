from django.contrib import admin
from .models import CountyManager

@admin.register(CountyManager)
class AgentAdmin(admin.ModelAdmin):
    pass
