from rest_framework import serializers
from .models import PerformanceReport, AttendanceReport

class PerformanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReport
        fields = ['id', 'student', 'grade', 'remarks', 'date']

class AttendanceReportSerializer(serializers.ModelSerializer):
    attendance_percentage = serializers.SerializerMethodField()

    class Meta:
        model = AttendanceReport
        fields = ['id', 'student', 'total_classes', 'classes_attended', 'attendance_percentage', 'date']

    def get_attendance_percentage(self, obj):
        return obj.attendance_percentage()
