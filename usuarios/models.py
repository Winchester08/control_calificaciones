from django.db import models

class usuarios(models.Model):
    nombre = models.CharField(max_length=10, verbose_name='Nombre Usuario')
    paterno = models.CharField(max_length=40, verbose_name='Paterno')
    materno = models.CharField(max_length=40, verbose_name='Materno')
    estatus = models.CharField(max_length=40, verbose_name='Estatus')
    usuario = models.CharField(max_length=10, verbose_name='usuario')
    clave = models.CharField(max_length=10, verbose_name='contrasena')
