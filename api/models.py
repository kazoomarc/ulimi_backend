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