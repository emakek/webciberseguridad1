'''
URL configuration for a_webciberseguridad1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
'''
from django.contrib import admin
from django.urls import path, include
from .views import base, inicio, contacto, categorias, acercade
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', base, name = 'base'),
    path('inicio/', inicio, name = 'inicio'),
    path('contacto/', contacto, name = 'contacto'),
    path('categorias/', categorias, name = 'categorias'),
    path('acercade/', acercade, name = 'acercade'),
    path('usuarios/', include('apps.usuarios.urls')),
    path('noticias/', include('apps.noticias.urls')),
    path('opiniones/', include('apps.opiniones.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

