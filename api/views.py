from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Crop, Task  
from .serializers import CropSerializer, TaskSerializer

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

# task viewSet
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer