from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('usuarios_captura', views.crear_usuario, name="alta_usuarios"),
    path('guarda_usuarios', views.guardado_usuarios, name='guarda_usuarios'),
    path('lista_usuarios/', views.consulta_usuarios, name='usuarios_lista')
]