from django.contrib import admin
from .models import Doctor, Paciente, Cita

admin.site.register(Doctor)
admin.site.register(Paciente)
admin.site.register(Cita)
