
from django.urls import path
from .views import *
urlpatterns = [
 path('', inicio, name='inicio'),
 path('autor/', crear_autor, name='crear_autor'),
 path('categoria/', crear_categoria, name='crear_categoria'),
 path('post/', crear_post, name='crear_post'),
 path('buscar/', buscar_post, name='buscar_post'),
]
