from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Company, Permission, Service, AvailableService
from .serializers import CompanySerializer, PermissionSerializer, ServiceSerializer, AvailableServiceSerializer


class CompanyView(viewsets.ModelViewSet):
    
    model = Company
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

class PermissionView(viewsets.ModelViewSet):
    
    model = Permission
    queryset=Permission.objects.all()
    serializer_class=PermissionSerializer

class ServiceView(viewsets.ModelViewSet):
    
    model = Service
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer

class AvailableServiceView(viewsets.ModelViewSet):
    
    model = AvailableService
    queryset=AvailableService.objects.all()
    serializer_class=AvailableServiceSerializer