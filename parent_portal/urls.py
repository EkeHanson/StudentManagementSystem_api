from django.urls import path
from .views import ParentListView, ParentDetailView, ParentCreateView

urlpatterns = [
    path('parents/', ParentListView.as_view(), name='parent-list'),
    path('parents/<int:pk>/', ParentDetailView.as_view(), name='parent-detail'),
    path('parents/create/', ParentCreateView.as_view(), name='parent-create'),
]
