from rest_framework import serializers
from .models import Teacher
from user_management.serializers import UserSerializer

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'subject_specialization', 'qualifications', 'years_of_experience']

class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['user', 'subject_specialization', 'qualifications', 'years_of_experience']
