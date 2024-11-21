from rest_framework import serializers
from .models import Bus, BusSchedule

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'plate_number', 'capacity', 'route', 'driver_name', 'driver_contact']

class BusScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSchedule
        fields = ['id', 'bus', 'stop', 'time']
