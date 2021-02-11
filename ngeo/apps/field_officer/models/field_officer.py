from django.db import models
from ngeo.apps.account.models import User
from ngeo.apps.shapefiles.models import IsioloProject

class FieldOfficer(models.Model):
    jurisdiction = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='field_officer')
    projects = models.ForeignKey(IsioloProject, on_delete=models.CASCADE, related_name='field_officer', null=True)