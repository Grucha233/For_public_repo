from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.


class WarehouseView(viewsets.ModelViewSet):
    model = Warehouse
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class CategoryView(viewsets.ModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MeasureUnitView(viewsets.ModelViewSet):
    model = MeasureUnit
    queryset = MeasureUnit.objects.all()
    serializer_class = MeasureUnitSerializer


class ProductView(viewsets.ModelViewSet):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class TransactionSerializer(viewsets.ModelViewSet):
    model = Transaction
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer