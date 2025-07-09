from django.urls import path
from django.contrib import admin

from .views import AgregarCategoria, AgregarNoticia, ListarNoticias, ModificarNoticia, EliminarNoticia, noticia_detalle, listar_por_categoria, ordenar_por

app_name = "apps.noticias"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar_categoria/', AgregarCategoria.as_view(), name='agregar_categoria'),
    path('agregar_noticia/', AgregarNoticia.as_view(), name='agregar_noticia'),
    path('listar_noticias/', ListarNoticias.as_view(), name='listar_noticias'),
    path('modificar_noticia/<int:pk>', ModificarNoticia.as_view(), name='modificar_noticia'),
    path('eliminar_Noticia/<int:pk>', EliminarNoticia.as_view(), name='eliminar_noticia'),
    path('detalle_noticia/<int:id>', noticia_detalle, name='detalle_noticia'),
    path("listar_por_categoria/<str:categoria>", listar_por_categoria, name='listar_por_categoria'),
    path("ordenar_por/", ordenar_por, name='ordenar_por'), 

]