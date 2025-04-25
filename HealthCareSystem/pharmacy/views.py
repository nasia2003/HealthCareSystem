# pharmacy/views.py
from rest_framework import viewsets
from .models import DispensedPrescription, DispenseStatus
from .serializers import DispensedPrescriptionSerializer, DispenseStatusSerializer

class DispensedPrescriptionViewSet(viewsets.ModelViewSet):
    queryset = DispensedPrescription.objects.all()
    serializer_class = DispensedPrescriptionSerializer


class DispenseStatusViewSet(viewsets.ModelViewSet):
    queryset = DispenseStatus.objects.all()
    serializer_class = DispenseStatusSerializer
