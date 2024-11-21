from django.db import models
from teacher_management.models import Teacher
from student_management.models import Student

class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="subjects")
    
    def __str__(self):
        return self.name

class Timetable(models.Model):
    class_assigned = models.CharField(max_length=50)
    day_of_week = models.CharField(max_length=10)  # E.g., Monday
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_assigned} - {self.subject.name} ({self.day_of_week})"
