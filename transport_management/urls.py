from django.urls import path
from .views import BusListView, BusScheduleListView

urlpatterns = [
    path('buses/', BusListView.as_view(), name='bus-list'),
    path('schedules/', BusScheduleListView.as_view(), name='bus-schedule-list'),
]
