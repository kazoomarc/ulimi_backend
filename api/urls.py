from django.urls import path
from rest_framework.routers import SimpleRouter
from  .views import CropViewSet, TaskViewSet, FinanceViewSet

# added
# urlpatterns = router.urls