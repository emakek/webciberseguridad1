from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from .views import ActualizarUsuario,EliminarUsuario,listar_usuarios, salir


app_name= "apps.usuarios"

urlpatterns = [
    path("registrar/", RegistrarUsuario.as_view(), name="registrar"),
    path("iniciar_sesion/", LoginView.as_view(template_name="usuarios/iniciar_sesion.html"), name="iniciar_sesion"),
    path("cerrar_sesion", LogoutView.as_view(), name="cerrar_sesion"),
    path("actualizar_usuario/<int:pk>", ActualizarUsuario.as_view(), name='actualizar_usuario'),
    path("eliminar_usuario/<int:pk>", EliminarUsuario.as_view(), name='eliminar_usuario'),
    path("listar_usuarios/", listar_usuarios, name='listar_usuarios'),
    path("salir/", salir, name='salir'),
]