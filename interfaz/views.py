from django.shortcuts import render
from django.http import HttpResponse

def principal(request):
    return HttpResponse("Interfaz de Calificaciones de Alumnos")
