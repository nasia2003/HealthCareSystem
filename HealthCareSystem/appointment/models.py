# appointment/models.py
import uuid
from django.db import models

class AppointmentStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient_id = models.UUIDField()
    doctor_id = models.UUIDField()
    scheduled_time = models.DateTimeField()
    status = models.ForeignKey(AppointmentStatus, on_delete=models.CASCADE)
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment {self.id} - {self.status.name}"
