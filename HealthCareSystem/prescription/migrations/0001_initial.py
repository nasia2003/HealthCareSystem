# Generated by Django 5.1.7 on 2025-04-24 06:21

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('patient_id', models.UUIDField()),
                ('doctor_id', models.UUIDField()),
                ('issued_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('drug_name', models.CharField(max_length=255)),
                ('dosage', models.CharField(max_length=100)),
                ('frequency', models.CharField(max_length=100)),
                ('duration_days', models.IntegerField()),
                ('instructions', models.TextField(blank=True)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medications', to='prescription.prescription')),
            ],
        ),
    ]
