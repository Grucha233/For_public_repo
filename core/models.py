from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Company(models.Model):
    name_pl_PL = models.TextField(blank=True, null=True)
    name_eng_US = models.TextField(blank=True, null=True)
    about_pl_PL = models.TextField(blank=True, null=True)
    about_eng_US = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone1 = models.TextField(blank=True, null=True)
    phone2 = models.TextField(blank=True, null=True)
    extra_contact_pl_PL = models.TextField(blank=True, null=True)
    extra_contact_eng_US = models.TextField(blank=True, null=True)


class Permission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.TextField(blank=True, null=True)
    name_pl_PL = models.TextField(blank=True, null=True)
    name_eng_US = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, related_name="permission", on_delete=CASCADE)


class Service(models.Model):
    name_pl_Pl = models.TextField(blank=True, null=True)
    name_eng_US = models.TextField(blank=True, null=True)
    about_pl_PL = models.TextField(blank=True, null=True)
    about_eng_US = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)

class AvailableService(models.Model):
    company = models.ForeignKey(Company, related_name="available_service", on_delete=CASCADE)
    service = models.ForeignKey(Service, on_delete=CASCADE)