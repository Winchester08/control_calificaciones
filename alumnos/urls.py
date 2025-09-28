from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/', views.ventana_alumnos, name='alumnos'),
    path('alumnos_consulta', views.consulta_alumnos, name='consulta_alumnos')
]