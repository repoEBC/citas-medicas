from django.urls import path
from . import views

urlpatterns = [
    path('citas/', views.appointments_view, name='appointments'),
    path('api/citas/', views.api_citas, name='api_citas'),
]