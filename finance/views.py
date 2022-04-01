from django.shortcuts import render
from rest_framework import viewsets
from models import *
from serializers import *

class CompanyView(viewsets.ModelViewSet):
    
    model = Finance
    queryset=Finance.objects.all()
    serializer_class=FinanceSerializer

class TransactionView(viewsets.ModelViewSet):
    
    model = Transaction
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer