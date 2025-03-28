from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # for http://127.0.0.1:8000/
    path('citas/', views.appointments_view, name='appointments'),
    path('api/citas/', views.api_citas, name='api_citas'),
]
