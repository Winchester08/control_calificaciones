from django.shortcuts import render
from django.http import HttpResponse

def ventana_alumnos(request):
    return HttpResponse("Ventana de Alumnos")
