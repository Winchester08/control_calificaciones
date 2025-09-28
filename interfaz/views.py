from django.shortcuts import render
from django.http import HttpResponse

def principal(request):
    titulo_ventana = 'Ventana de la Interfaz Principal'
    titulo = 'Control de Calificaciones'
    return render (request, 'interfaz/interfaz.html',{
        "titulo" : titulo_ventana,
        "sistema": titulo
    })
