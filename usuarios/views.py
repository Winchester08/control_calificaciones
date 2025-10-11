from django.shortcuts import render
from django.http import HttpResponse
from .models import usuarios

def login(request):
    return HttpResponse("Login de Usuarios")

def crear_usuario(request):
    titulo = "Captura de Usuarios"
    return render(request, "usuarios/captura.html",{
        "ventana" : titulo
    })

def guardado_usuarios(request):
    if request.method == 'POST':
        nom = request.POST.get('nombre')
        p = request.POST.get('paterno')
        m = request.POST.get('materno')
        es = request.POST.get('estatus')
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')
        guarda = usuarios(nombre = nom, paterno=p, materno=m, estatus=es, usuario=usuario, clave=clave )
        guarda.save()
        print("Datos guardados con exito")
        return HttpResponse("Datos guardados con exito")
    else:
        return HttpResponse("Existe un error en el guardado")

def consulta_usuarios(request):
    titulo = "Listado de Usuarios"
    listado_usuarios = usuarios.objects.all()
    return render(request, 'usuarios/listado_usuarios.html',{
        'ventana':titulo,
        'listado':listado_usuarios
    })
