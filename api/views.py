from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Crop, Task, Finance, Produce, LivestockType, Livestock
from .serializers import CropSerializer, TaskSerializer, FinanceSerializer, ProduceSerializer,  LivestockTypeSerializer, LivestockSerializer

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

# task viewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# finance viewset
class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer

# produce viewset
class ProduceViewSet(viewsets.ModelViewSet):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer

# livestockType viewset
class LivestockTypeViewSet(viewsets.ModelViewSet):
    queryset = LivestockType.objects.all()
    serializer_class = LivestockTypeSerializer