from django.db import models

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

class Cita(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, default="Programada")

    def __str__(self):
        return f"{self.paciente.nombre} con {self.doctor.nombre} el {self.fecha} a las {self.hora}"

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"

