# ehr/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, MedicalRecordViewSet, AllergyViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'records', MedicalRecordViewSet)
router.register(r'allergies', AllergyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
