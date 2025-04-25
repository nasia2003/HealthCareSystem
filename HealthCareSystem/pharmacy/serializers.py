# pharmacy/serializers.py
from rest_framework import serializers
from .models import DispensedPrescription, DispenseStatus

class DispenseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispenseStatus
        fields = '__all__'

class DispensedPrescriptionSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(queryset=DispenseStatus.objects.all())

    class Meta:
        model = DispensedPrescription
        fields = '__all__'
