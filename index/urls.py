from django.urls import path
from . import views



#Creamos la lista de urls

urlspatterns = [
    path('index', views.index, name='index'),#Cuando se acceda a la url /gatos/index se ejecutará la función index del archivo views.py
]