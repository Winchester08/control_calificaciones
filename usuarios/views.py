from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("Login de Usuarios")

def crear_usuario(request):
    titulo = "Captura de Usuarios"
    return render(request, "usuarios/captura.html",{
        "ventana" : titulo
    })

def consulta_usuarios(request):
    return HttpResponse("Consulta Usuarios")
