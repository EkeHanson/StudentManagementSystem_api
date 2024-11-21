from django.urls import path
from .views import SubjectListView, TimetableListView

urlpatterns = [
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('timetable/', TimetableListView.as_view(), name='timetable-list'),
]
