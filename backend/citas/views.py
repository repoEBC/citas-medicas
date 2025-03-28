from django.http import JsonResponse
from .models import Cita
from django.shortcuts import render


def home(request):
    return render(request, 'index2.html')

def appointments_view(request):
    return render(request, 'appointments.html')

def api_citas(request):
    citas = Cita.objects.select_related('paciente', 'doctor').all()
    data = []

    for cita in citas:
        data.append({
            'nombre_paciente': cita.paciente.nombre if cita.paciente else "Sin paciente",
            'fecha': cita.fecha.strftime('%Y-%m-%d') if cita.fecha else "Sin fecha",
            'hora': cita.hora.strftime('%H:%M') if cita.hora else "Sin hora",
            'motivo': cita.motivo or "Sin motivo",
        })

    return JsonResponse(data, safe=False)