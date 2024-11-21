from django.db import models
from user_management.models import CustomUser

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="student_profile")
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    class_assigned = models.CharField(max_length=50)
    section = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
