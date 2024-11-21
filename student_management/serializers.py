from rest_framework import serializers
from .models import Student
from user_management.serializers import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ['id', 'user', 'date_of_birth', 'address', 'class_assigned', 'section']

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user', 'date_of_birth', 'address', 'class_assigned', 'section']
