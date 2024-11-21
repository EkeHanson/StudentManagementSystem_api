from django.db import models
from user_management.models import CustomUser
from student_management.models import Student

class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="parent_profile")
    children = models.ManyToManyField(Student, related_name="parents")

    def __str__(self):
        return self.user.get_full_name()
