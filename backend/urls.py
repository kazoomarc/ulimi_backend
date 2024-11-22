"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    CropViewSet, TaskViewSet,
    FinanceViewSet, ProduceViewSet,
    LivestockTypeViewSet, LivestockViewSet,
    CropViewSet, CropInStorageViewSet, CropHarvestedViewSet
)


router = DefaultRouter()
router.register(r'crops', CropViewSet)
router.register(r'crops-in-storage', CropInStorageViewSet)
router.register(r'crops-harvested', CropHarvestedViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'finances', FinanceViewSet)
router.register(r'produces', ProduceViewSet)
router.register(r'livestock-types', LivestockTypeViewSet)
router.register(r'livestock', LivestockViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
]
