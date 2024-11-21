from django.urls import path
from .views import StudentListView, StudentDetailView, StudentCreateView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/create/', StudentCreateView.as_view(), name='student-create'),
]