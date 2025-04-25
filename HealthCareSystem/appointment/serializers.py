# appointment/serializers.py
from rest_framework import serializers
from .models import Appointment, AppointmentStatus

class AppointmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentStatus
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    status = AppointmentStatusSerializer()

    class Meta:
        model = Appointment
        fields = '__all__'
