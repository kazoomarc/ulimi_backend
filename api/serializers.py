from rest_framework import serializers
from .models import (
    Crop, Task, Finance, Produce,
    LivestockType, Livestock,
    Crop, CropInStorage, CropHarvested
)

# Crop Serializer
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

# CropInStorage Serializer
class CropInStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropInStorage
        fields = '__all__'

# CropHarvested Serializer
class CropHarvestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropHarvested
        fields = '__all__'

# task serializer
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# finance serializer

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'

# produce serializer

class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = '__all__'

# LivestockType serializer

class LivestockTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockType
        fields = '__all__'

# livestock serializer
class LivestockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livestock
        fields = '__all__'