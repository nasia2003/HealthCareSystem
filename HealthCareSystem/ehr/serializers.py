# ehr/serializers.py
from rest_framework import serializers
from .models import Patient, MedicalRecord, Allergy

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'

class AllergySerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergy
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    records = MedicalRecordSerializer(many=True, read_only=True)
    allergies = AllergySerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'