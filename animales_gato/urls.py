from django.urls import path
from . import views



#Creamos la lista de urls

urlspatterns = [
    path('animales_gato', views.animales_gato, name='animales_gato'),
]