from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Crop, Task, Finance, Produce
from .serializers import CropSerializer, TaskSerializer, FinanceSerializer, ProduceSerializer

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