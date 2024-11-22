from django.urls import path
from rest_framework.routers import SimpleRouter
from  .views import (
    CropViewSet,CropInStorageViewSet, CropHarvestedViewSet,
    TaskViewSet, FinanceViewSet, 
    LivestockTypeViewSet, LivestockViewSet
)


# added
# urlpatterns = router.urls