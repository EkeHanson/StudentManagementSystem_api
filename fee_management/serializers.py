from rest_framework import serializers
from .models import Fee

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = ['id', 'student', 'amount', 'due_date', 'status']