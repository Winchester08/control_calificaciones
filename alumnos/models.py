from django.db import models

class alumnos(models.Model):
    matricula = models.CharField(max_length=20, verbose_name="Matricula")
    cuatrimestre = models.CharField(max_length=20,verbose_name="Cuatrimestre")
    nombre = models.CharField(max_length=40,verbose_name="Nombre alumno")
    paterno = models.CharField(max_length=40,verbose_name="Paterno")
    materno = models.CharField(max_length=40,verbose_name="Materno")
    estatus = models.CharField(max_length=20, verbose_name="Matricula")
