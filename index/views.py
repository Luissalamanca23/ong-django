from django.shortcuts import render, get_object_or_404
from .models import Gato

def index(request):
    contexto = {'mensaje': 'Pagina de inicio'}
    return render(request, 'index.html')

def animales_gato(request):
    contexto = {'mensaje': 'Pagina de gatos'}
    return render(request, 'animales_gato.html')

def animales_perro(request):
    contexto = {'mensaje': 'Pagina de perros'}
    return render(request, 'animales_perro.html')

def perros(request):
    contexto = {'mensaje': 'Pagina de perros'}
    return render(request, 'perros.html')

def gato(request, slug):
    gato = get_object_or_404(Gato, slug=slug)
    contexto = {'gato': gato, 'mensaje': 'Pagina de gatos'}
    return render(request, 'gatos.html', contexto)

def login(request):
    contexto = {'mensaje': 'Pagina de login'}
    return render(request, 'login.html')