from django.urls import path
from .views import FeeListView

urlpatterns = [
    path('fees/', FeeListView.as_view(), name='fee-list'),
]
