"""
URL configuration for myproject project.

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
"""
from django.contrib import admin
from django.urls import path, include
from index.views import *

urlpatterns = [
    path('admin/', admin.site.urls),  # Esta línea conecta todas las rutas de administración de Django.
    path('', index),  # Esta línea conecta la ruta raíz ('') a la vista 'index'.
    path('animales_gato/', animales_gato),  # Esta línea conecta la ruta 'animales_gato/' a la vista 'animales_gato'.
    path('animales_perro/', animales_perro),  # Esta línea conecta la ruta 'animales_perro/' a la vista 'animales_perro'.
    path('animales_gato/gato/<slug:slug>/', gato, name='gato'),  # Esta línea conecta la ruta 'animales_gato/gato/<slug:slug>/' a la vista 'gato'. El '<slug:slug>' es un parámetro que se pasará a la vista 'gato'.
    path('animales_perro/perros/', perros),  # Esta línea conecta la ruta 'animales_perro/perros/' a la vista 'perros'.
    path('login/', login),  # Esta línea conecta la ruta 'login/' a la vista 'login'.
]