from django.db.models import fields
from rest_framework import serializers

from .models import Company, Permission


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"

class AvailableServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"