from django.db import models
from ngeo.apps.account.models import User

class FieldOfficer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="field_officer")
    