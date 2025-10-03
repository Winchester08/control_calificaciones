from django.urls import path
from . import views

urlpatterns = [
    path('alumnos/', views.ventana_alumnos, name='alumnos'),
    path('alumnos_consulta/', views.consulta_alumnos, name='consulta_alumnos'),
    path('captura_calificacion/', views.captura_calificaciones, name='captura_calificacion'),
    path('consulta_calificacion/', views.consulta_calificaciones, name='consulta_calificacion'),
]