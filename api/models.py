from django.db import models

# Create your models here.
from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    planting_date = models.DateField(null=True, blank=True)
    harvest_duration = models.IntegerField(help_text="Estimated days to harvest", null=True)
    is_seasonal = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# task model
class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

# finance model

class Finance(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.type} - ${self.amount} on {self.date}"


# produce model
class Produce(models.Model):
    type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_collected = models.DateField()

    def __str__(self):
        return f"{self.type} - {self.amount} on {self.date_collected}"

# livestockType model
class LivestockType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# livestock model
class Livestock(models.Model):
    VACCINATION_STATUS = [
        ('vaccinated', 'Vaccinated'),
        ('not_vaccinated', 'Not Vaccinated'),
        ('due', 'Due for Vaccination'),
    ]
    
    type = models.ForeignKey(LivestockType, on_delete=models.CASCADE, related_name='livestock')
    date_of_birth = models.DateField()
    vaccination_status = models.CharField(max_length=20, choices=VACCINATION_STATUS)

    def __str__(self):
        return f"{self.type} - Born: {self.date_of_birth}"