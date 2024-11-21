from django.db import models
from student_management.models import Student

class PerformanceReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="performance_reports")
    grade = models.CharField(max_length=5)
    remarks = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.student.user.get_full_name()} on {self.date}"

class AttendanceReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance_reports")
    total_classes = models.IntegerField()
    classes_attended = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def attendance_percentage(self):
        return (self.classes_attended / self.total_classes) * 100 if self.total_classes > 0 else 0

    def __str__(self):
        return f"Attendance for {self.student.user.get_full_name()} - {self.date}"
