from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING
from core.models import Company
from datetime import datetime  
# Create your models here.

class Warehouse(models.Model):
    company = models.OneToOneField(Company, related_name="warehouse", on_delete=CASCADE)

class Category(models.Model):
    warehouse = models.ForeignKey(Warehouse, related_name="categories", on_delete=CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    parent_category = models.ForeignKey("Category", related_name="parent_category", on_delete=CASCADE)


class MeasureUnit(models.Model):
    warehouse = models.ForeignKey(Warehouse, related_name="measure_units", on_delete=CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)


    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=CASCADE)
    measure_unit = models.ForeignKey(MeasureUnit, related_name="products", on_delete=CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.IntegerField(null=True, blank=True)
    approximate_price = models.DecimalField(decimal_places=2, null=True, blank=True)


class Transaction(models.Model):
    warehouse = models.ForeignKey(Warehouse, related_name="transactions", on_delete=CASCADE)
    product = models.ForeignKey(Product, related_name="transactions", on_delete=CASCADE)
    date = models.DateField(default=datetime.now() ,blank=True, null=True)
    amount = models.IntegerField(defualt=0, null=True, blank=True)
   
