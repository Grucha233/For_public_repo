from django.shortcuts import render
from rest_framework import viewsets
from models import *
from serializers import *

class CompanyView(viewsets.ModelViewSet):
    
    model = OwnerPanelLog
    queryset=OwnerPanelLog.objects.all()
    serializer_class=OwnerPanelLogSerializer