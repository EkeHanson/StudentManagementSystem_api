from rest_framework import generics
from .models import Bus, BusSchedule
from .serializers import BusSerializer, BusScheduleSerializer

class BusListView(generics.ListAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class BusScheduleListView(generics.ListAPIView):
    queryset = BusSchedule.objects.all()
    serializer_class = BusScheduleSerializer
