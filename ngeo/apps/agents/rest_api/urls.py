from django.urls import path

from .views import AgentDetail, AgentListCreate, AgentReturnDetail, AgentReturnListCreate

urlpatterns = [
    path("agents", AgentListCreate.as_view(), name="agents"),
    path("agents/<int:pk>", AgentDetail.as_view(), name="agents-detail"),
    path("agent-returns", AgentReturnListCreate.as_view(), name="agent-return"),
    path("agent-returns/<int:pk>", AgentReturnDetail.as_view(), name="agent-return-detail"),
]
