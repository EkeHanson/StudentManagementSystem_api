from django.urls import path
from .views import TeacherListView, TeacherDetailView, TeacherCreateView

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher-create'),
]
