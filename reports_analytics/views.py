from rest_framework import generics
from .models import PerformanceReport, AttendanceReport
from .serializers import PerformanceReportSerializer, AttendanceReportSerializer

class PerformanceReportListView(generics.ListAPIView):
    queryset = PerformanceReport.objects.all()
    serializer_class = PerformanceReportSerializer

class AttendanceReportListView(generics.ListAPIView):
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer
