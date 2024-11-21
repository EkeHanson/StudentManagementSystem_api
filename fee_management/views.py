from rest_framework import generics
from .models import Fee
from .serializers import FeeSerializer

class FeeListView(generics.ListAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer
