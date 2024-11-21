from rest_framework import serializers
from .models import Subject, Timetable

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'teacher']

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = ['id', 'class_assigned', 'day_of_week', 'subject', 'start_time', 'end_time']
