from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import (
    Crop, Task, Finance, Produce,
    LivestockType, Livestock,
    Crop, CropInStorage, CropHarvested,
    Message
)

from .serializers import (
    CropSerializer, TaskSerializer,
    FinanceSerializer, ProduceSerializer,
    LivestockTypeSerializer, LivestockSerializer,
    CropSerializer, CropInStorageSerializer, CropHarvestedSerializer,
    MessageSerializer
)

# Crop ViewSet
class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

# CropInStorage ViewSet
class CropInStorageViewSet(viewsets.ModelViewSet):
    queryset = CropInStorage.objects.all()
    serializer_class = CropInStorageSerializer

# CropHarvested ViewSet
class CropHarvestedViewSet(viewsets.ModelViewSet):
    queryset = CropHarvested.objects.all()
    serializer_class = CropHarvestedSerializer

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

# livestock viewset
class LivestockViewSet(viewsets.ModelViewSet):
    queryset = Livestock.objects.all()
    serializer_class = LivestockSerializer

# message viewset
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer