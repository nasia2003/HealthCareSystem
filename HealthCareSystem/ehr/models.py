# ehr/models.py
import uuid
from django.db import models

class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class MedicalRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='records')
    diagnosis = models.TextField()
    treatment = models.TextField()
    doctor_notes = models.TextField()
    recorded_at = models.DateTimeField(auto_now_add=True)

class Allergy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='allergies')
    substance = models.CharField(max_length=100)
    reaction = models.CharField(max_length=200)
    noted_at = models.DateTimeField(auto_now_add=True)
