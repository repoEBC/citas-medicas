from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(default='12:00')  # ✅ valid HH:MM default
    motivo = models.CharField(max_length=255, default='Consulta general')
    status = models.CharField(max_length=20, default="Scheduled")

