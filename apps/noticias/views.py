from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponsePermanentRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse

from .models import Categoria, Noticias
from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm

#create your views here.

class AgregarCategoria(CreateView):
    model = Categoria
    fields = {"nombre"}
    template_name = "noticias/agregar_categoria.html"
    succes_url = reverse_lazy("inicio")

class AgregarNoticia(CreateView):
    model = Noticias
    fields = ["titulo", "autor", "informacion", "fecha_agregado", "categoria", "imagen" ]
    template_name = "noticias/agregar_noticia.html"
    success_url = reverse_lazy("inicio")

    def form_valid(self, form):
        form.instance.colaborador = self.request.user
        return super().form_valid(form)
    
class ModificarNoticia(UpdateView):
    model = Noticias
    fields = ["titulo", "autor", "informacion", "fecha_agregado", "categoria", "imagen" ]
    template_name = "noticias/agregar_noticia.html"
    success_url = reverse_lazy("inicio")
    
class ListarNoticias(ListView):
    model = Noticias
    template_name = "noticias/listar_noticias.html"
    context_object_name = "noticias"

    def get_context_data(self) :
        context = super().get_context_data()
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context

    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains = query)
        return queryset.order_by('titulo')

class EliminarNoticia(DeleteView):
    model = Noticias
    template_name = "noticias/confirma_eliminar.html"
    success_url = reverse_lazy("inicio")

#class NoticiaDetalle(DetailView):
#    model = Noticias
#    template_name = "noticias/noticia_detalle.html"
#    context_object_name = "noticia"

def noticia_detalle(request, id):
    noticia = Noticias.objects.get(id=id)
    opiniones = Opinion.objects.filter(noticia=id)
    form = OpinionForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.noticia = noticia
            aux.usuario = request.user
            aux.save()
            detalle_url = reverse('apps.noticias:detalle_noticia', kwargs={'id': noticia.id})
            return HttpResponsePermanentRedirect(detalle_url)
        else:
            return redirect("apps.usuarios:iniciar_sesion")
    contexto = {
        "noticia" : noticia,
        "form" : form,
        "opiniones" : opiniones
    }
    template_name ="noticias/noticia_detalle.html"
    return render(request, template_name, contexto)

def listar_por_categoria(request, categoria):
    categoria = Categoria.objects.filter(nombre = categoria)
    noticias = Noticias.objects.filter(categoria = categoria[0].id).order_by('fecha_agregado')
    categorias = Categoria.objects.all()
    template_name = 'noticias/listar_noticias.html'
    contexto = {
        'noticias' : noticias,
        'categorias' : categorias        
    }
    return render(request,template_name,contexto)

def ordenar_por(request):
    # Obtenemos el dato de 'orden' de la URL -> metodo GET ( para esto tiene que haber un elemento html que contenga el name = 'orden' y el valor(value=''))
    orden = request.GET.get('orden', '')
    #Validar lo que contiene Value
    if orden == 'fecha':
        noticias = Noticias.objects.order_by('fecha_agregado')
    elif orden == 'titulo':
        noticias = Noticias.objects.order_by('titulo')
    else:
        noticias = Noticias.objects.all()
    categorias = Categoria.objects.all()
    template_name = 'noticias/listar_noticias.html'
    contexto = {
        'noticias' : noticias,
        'categorias' : categorias,
    }
    return render(request, template_name, contexto)



