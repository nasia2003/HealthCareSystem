# prescription/models.py
import uuid
from django.db import models

class Prescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.UUIDField()
    doctor_id = models.UUIDField()
    issued_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Rx {self.id} - Patient {self.patient_id}"


class Medication(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    prescription = models.ForeignKey(Prescription, related_name='medications', on_delete=models.CASCADE)
    drug_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)  # e.g., "500mg"
    frequency = models.CharField(max_length=100)  # e.g., "twice a day"
    duration_days = models.IntegerField()
    instructions = models.TextField(blank=True)

    def __str__(self):
        return f"{self.drug_name} for Rx {self.prescription.id}"
