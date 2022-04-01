from django.db import models

class Finance(models.Model):

    balance = models.DecimalField(blank=True, null=True)


class Transaction(models.Model):

    finance = models.ForeignKey(Finance)
    datetime = models.DateTimeField(blank=True, null=True)
    status = models.TextField(blank=True,null=True)
    amount = models.DecimalField(blank=True,null=True)
    balanceAfter = models.DecimalField(blank=True, null=True)
    description_pl_PL = models.TextField(blank=True, null=True)
    description_eng_US = models.TextField(blank=True, null=True)
    