from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages

from .models import Usuarios
from .forms import RegistrarUsuariosForm

# Create your views here.
class RegistrarUsuario(CreateView):
    model = Usuarios
    form_class = RegistrarUsuariosForm
    template_name = "usuarios/registrar_usuarios.html"
    succes_url = reverse_lazy('inicio')

class ActualizarUsuario(LoginRequiredMixin,UpdateView):
    model = Usuarios
    fields= ['nombre','apellido','email','fecha_nacimiento', 'imagen']
    template_name = 'usuarios/registrar_usuarios.html'
    success_url = reverse_lazy('inicio')

class EliminarUsuario(LoginRequiredMixin,DeleteView):
    model = Usuarios
    template_name = 'noticias/confirma_eliminar.html'
    success_url = reverse_lazy('apps.usuarios:listar_usuarios')

def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    template_name = 'usuarios/listar_usuarios.html'
    contexto = {
        "usuarios" : usuarios
    }
    return render(request, template_name, contexto)

def salir(request):
    logout(request)
    messages.success(request, F"tu sesión se ha cerrado correctamente")
    return redirect('inicio')
    





