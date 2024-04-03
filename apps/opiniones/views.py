from typing import Any
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView

from .forms import OpinionForm
from .models import Opinion

# Create your views here.

def AgregarOpinion(request):
    form = OpinionForm(request.Post or None)
    if form.is_valid():
        form.save()
    contexto = {
        'form' : form,
    }

    template_name = "opiniones/agregar_opinion.html"
    return render(request, template_name, contexto)

class ModificarOpinion(LoginRequiredMixin, UpdateView):
    model = Opinion
    fields = ["texto"]
    template_name = "opiniones/modificar_opinion.html"
    
    def get_success_url(self):
        detalle_url = reverse("apps.noticias:detalle_noticia", kwargs={"id": self.object.noticia.id})
        return detalle_url
    
    def get_context_data(self):
        context = super().get_context_data()
        noticia = self.object.noticia
        opiniones = Opinion.objects.filter(noticia=noticia.id)
        context["noticia"] = noticia
        context["opiniones"] = opiniones
        return  context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario=self.request.user)
    
class EliminarOpinion(LoginRequiredMixin, DeleteView):
    model = Opinion
    template_name = "opiniones/eliminar_opinion.html"
    context_object_name = "opinion"
   
    
    def get_success_url(self):
        detalle_url = reverse("apps.noticias:detalle_noticia", kwargs={'id': self.object.noticia.id})
        return detalle_url