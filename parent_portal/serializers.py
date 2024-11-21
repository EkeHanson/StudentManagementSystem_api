from rest_framework import serializers
from .models import Parent
from student_management.serializers import StudentSerializer
from user_management.serializers import UserSerializer

class ParentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    children = StudentSerializer(many=True)

    class Meta:
        model = Parent
        fields = ['id', 'user', 'children']

class ParentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['user', 'children']
