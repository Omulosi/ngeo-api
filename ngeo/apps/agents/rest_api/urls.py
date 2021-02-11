from django.urls import path
from .views import AgentDetail, AgentListCreate


urlpatterns = [
    path("agents", AgentListCreate.as_view(), name="agents")
]