from django.shortcuts import render
from django.http import HttpResponse

def ventana_alumnos(request):
    return HttpResponse("Ventana de Captura de Alumnos")


def consulta_alumnos(request):
    return HttpResponse("Ventana de Consulta de Alumnos")
