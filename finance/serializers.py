from rest_framework import serializers

from .models import *


class FinanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Finance
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = "__all__"