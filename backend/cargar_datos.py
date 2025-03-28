import os
import django
from datetime import datetime, timedelta
import random

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'citas_medicas.settings')
django.setup()

from citas.models import Doctor, Paciente, Cita

# Borra datos anteriores (opcional)
Doctor.objects.all().delete()
Paciente.objects.all().delete()
Cita.objects.all().delete()

# Crea doctores
doctores = [
    Doctor(nombre="Dra. Ana Torres", especialidad="Medicina General"),
    Doctor(nombre="Dr. Carlos Méndez", especialidad="Pediatría"),
    Doctor(nombre="Dr. Sofía Ruiz", especialidad="Cardiología"),
]
Doctor.objects.bulk_create(doctores)

# Crea pacientes
pacientes = [
    Paciente(nombre="Juan Pérez", email="juan@example.com"),
    Paciente(nombre="Laura García", email="laura@example.com"),
    Paciente(nombre="Miguel Torres", email="miguel@example.com"),
]
Paciente.objects.bulk_create(pacientes)

# Crea citas
motivos = ["Chequeo general", "Dolor de cabeza", "Consulta pediátrica", "Control de presión", "Dolor de pecho"]
estados = ["Programada", "Completada", "Cancelada"]

for i in range(10):
    Cita.objects.create(
        doctor=random.choice(Doctor.objects.all()),
        paciente=random.choice(Paciente.objects.all()),
        fecha=datetime.now().date() + timedelta(days=i),
        hora=(datetime.now() + timedelta(minutes=30 * i)).time(),
        motivo=random.choice(motivos),
        estado=random.choice(estados)
    )

print("✅ Datos de prueba cargados con éxito.")
