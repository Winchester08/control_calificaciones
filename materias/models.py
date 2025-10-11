from django.db import models

class materias(models.Model):
    clave_materia = models.CharField(max_length=10,verbose_name="Clave Materia")
    materia = models.CharField(max_length=50,verbose_name="Nombre Materia")
    cuatrimestre = models.CharField(max_length=20,verbose_name="Cuatrimestre")
    creditos = models.CharField(max_length=10,verbose_name="Creditos")

class calificaciones(models.Model):
    matricula = models.CharField(max_length=20, verbose_name="Matricula")
    clave_materia = models.CharField(max_length=10,verbose_name="Clave Materia")
    c1 = models.CharField(max_length=10, verbose_name="calificacion 1")
    c2 = models.CharField(max_length=10, verbose_name="calificacion 2")
    final = models.CharField(max_length=10, verbose_name="final")
    especial = models.CharField(max_length=10, verbose_name="extra")
