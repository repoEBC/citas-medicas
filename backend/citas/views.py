from django.http import JsonResponse
from .models import Appointment
from django.shortcuts import render

def appointments_view(request):
    return render(request, 'appointments.html')

def api_citas(request):
    citas = Appointment.objects.select_related('patient').all()
    data = []
    for cita in citas:
        data.append({
            'nombre_paciente': cita.patient.name if cita.patient else "Sin paciente",
            'fecha': cita.date.strftime('%Y-%m-%d') if cita.date else "Sin fecha",
            'hora': cita.time.strftime('%H:%M') if cita.time else "Sin hora",
            'motivo': cita.motivo or "Sin motivo",
        })
    return JsonResponse(data, safe=False)