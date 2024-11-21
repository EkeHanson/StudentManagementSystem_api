from django.urls import path
from .views import PerformanceReportListView, AttendanceReportListView

urlpatterns = [
    path('performance-reports/', PerformanceReportListView.as_view(), name='performance-reports'),
    path('attendance-reports/', AttendanceReportListView.as_view(), name='attendance-reports'),
]
