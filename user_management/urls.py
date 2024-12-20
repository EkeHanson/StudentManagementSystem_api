from django.urls import path
from .views import UserListView, UserDetailView, UserRegistrationView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]
