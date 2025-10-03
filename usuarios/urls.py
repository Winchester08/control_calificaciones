from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('usuarios_captura', views.crear_usuario, name="alta_usuarios"),
    path('usuarios_consulta', views.consulta_usuarios, name='consulta_usuarios')
]