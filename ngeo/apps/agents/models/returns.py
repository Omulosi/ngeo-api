from django.db import models
from django.core import validators
from ngeo.apps.projects.models import Project
from ngeo.apps.agents.models import Agent


class AgentReturn(models.Model):
    date_submitted = models.DateTimeField(verbose_name='submission date', null=True, blank=True)
    project = models.OneToOneField(Project, null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.IntegerField(null=True, blank=True, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)])
    progress_report = models.FileField(null=True, blank=True)
    # Each return is associated with an agent
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name="returns")

    class Meta:
        verbose_name_plural = "Agent Returns"
