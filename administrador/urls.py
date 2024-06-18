from django.urls import path
from . import views

urlpatterns =  [
    path('', views.administrador, name='administrador'),
    path('ruta/agregarMascota/', views.agregarMascota, name='agregarMascota'),
]