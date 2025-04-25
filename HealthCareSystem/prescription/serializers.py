# prescription/serializers.py
from rest_framework import serializers
from .models import Prescription, Medication

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(many=True)

    class Meta:
        model = Prescription
        fields = '__all__'

    def create(self, validated_data):
        medications_data = validated_data.pop('medications')
        prescription = Prescription.objects.create(**validated_data)
        for med_data in medications_data:
            Medication.objects.create(prescription=prescription, **med_data)
        return prescription
