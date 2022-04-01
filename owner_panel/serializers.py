from rest_framework import serializers

from .models import *


class OwnerPanelLogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OwnerPanelLog
        fields = "__all__"