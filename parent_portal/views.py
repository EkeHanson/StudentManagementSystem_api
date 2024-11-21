from rest_framework import generics
from .models import Parent
from .serializers import ParentSerializer, ParentCreateSerializer

class ParentListView(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentCreateView(generics.CreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentCreateSerializer
