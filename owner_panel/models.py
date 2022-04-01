from tkinter import CASCADE
from django.db import models
from core.models import Company
from django.contrib.auth.models import User

class OwnerPanelLog(models.Model):

    company = models.ForeignKey(Company, related_name="permission", on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)
    action_params = models.TextField(blank=True, null=True)

