from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Crop, Task, Finance
from .serializers import CropSerializer, TaskSerializer, FinanceSerializer

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