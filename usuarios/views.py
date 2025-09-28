from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("Login de Usuarios")

def crear_usuario(request):
    return HttpResponse("Captura de Usuarios nuevos")

def consulta_usuarios(request):
    return HttpResponse("Consulta Usuarios")
