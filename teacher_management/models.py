from django.db import models
from user_management.models import CustomUser

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="teacher_profile")
    subject_specialization = models.CharField(max_length=100)
    qualifications = models.TextField()
    years_of_experience = models.IntegerField()

    def __str__(self):
        return self.user.get_full_name()
