from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Crop, Task, Finance, Produce

admin.site.register(Crop)
admin.site.register(Task)
admin.site.register(Finance)
admin.site.register(Produce)