from django.shortcuts import render

def base(request):
    template_name = "base.html"
    return render (request, template_name)

def inicio(request):
    template_name = "inicio.html"
    return render(request, template_name)

def contacto(request):
    template_name = "contacto.html"
    return render(request, template_name)

def acercade(request):
    template_name = "acercade.html"
    return render(request, template_name)

def categorias(request):
    template_name = "categorias.html"
    return render(request, template_name)