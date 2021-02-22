from django.db import models
from ngeo.apps.account.models import User

class CountyManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="county_manager")