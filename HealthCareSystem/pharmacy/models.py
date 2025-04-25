# pharmacy/models.py
import uuid
from django.db import models

class DispenseStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class DispensedPrescription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    prescription_id = models.UUIDField()  # lấy từ Prescription Service
    pharmacist_id = models.UUIDField()
    dispensed_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(DispenseStatus, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Dispensed Rx {self.prescription_id}"
