# pharmacy/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DispensedPrescriptionViewSet, DispenseStatusViewSet

router = DefaultRouter()
router.register(r'dispensed', DispensedPrescriptionViewSet)
router.register(r'status', DispenseStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
