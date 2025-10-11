from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from materias.models import materias
from interfaz.models import alumnos


def ventana_alumnos(request):
    ventana='Captura de Alumnos'
    cuatrimestres = range(1,11)
    return render(request, 'alumnos/captura_alumnos.html',{
        "ventana": ventana,
        "cuatris": cuatrimestres
    })

def guardado_alumno(request):
    ms = 'Guardado Exitoso'
    if request.method == "POST":
        m = request.POST.get('matricula')
        c = request.POST.get('cuatrimestre')
        nom = request.POST.get('nombre')
        nomp = request.POST.get('paterno')
        nomm = request.POST.get('materno')
        es = request.POST.get('estatus')
        guardado = alumnos(matricula = m, cuatrimestre = c, nombre=nom, paterno=nomp, 
                           materno=nomm, estatus=es)
        guardado.save()
        return render(request, 'alumnos/exito.html', {
            "mensaje": ms
        })
    else:
        return HttpResponse("Error en el guardado del alumno")

def consulta_alumnos(request):
    ventana = 'Consulta Alumnos'
    lista_alumnos = alumnos.objects.all()
    # Select * from alumnos 
    return render(request, 'alumnos/consulta_alumnos.html',{
        "ventana":ventana,
        "alumnos":lista_alumnos
    })

def captura_calificaciones(request):
    ventana = 'Captura Calificaciones'
    semestres = range(1,11)
    
    return render(request, 'alumnos/captura_calificacion.html',{
        'ventana': ventana,
        'semestre': semestres
    })

def obtener_materias(request):
    cuatrimestre = request.GET.get('cuatri')
    materia = materias.objects.filter(cuatrimestre = cuatrimestre).values('id', 'cuatrimestre')
    
    return JsonResponse(list(materia), safe=False)

def consulta_calificaciones(request):
    ventana = 'Consulta Calificaciones'
    return render(request, 'alumnos/consulta_calificacion.html',{
        'ventana': ventana
    })