from django.shortcuts import render
from django.http import HttpResponse

def ventana_alumnos(request):
    ventana='Captura de Alumnos'
    return render(request, 'alumnos/captura_alumnos.html',{
        "ventana": ventana
    })


def consulta_alumnos(request):
    ventana = 'Consulta Alumnos'
    return render(request, 'alumnos/consulta_alumnos.html',{
        "ventana":ventana
    })

def captura_calificaciones(request):
    ventana = 'Captura Calificaciones'
    return render(request, 'alumnos/captura_calificacion.html',{
        'ventana': ventana
    })

def consulta_calificaciones(request):
    ventana = 'Consulta Calificaciones'
    return render(request, 'alumnos/consulta_calificacion.html',{
        'ventana': ventana
    })