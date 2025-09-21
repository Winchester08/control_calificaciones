from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/', views.ventana_alumnos, name='alumnos')
]