from django.shortcuts import render

# Create your views here.


def index(retquest):
    contexto = {'mensaje': 'Pagina de inicio'}
    return render(retquest, 'index.html');

def animales_gato(retquest):
    contexto = {'mensaje': 'Pagina de gatos'}
    return render(retquest, 'animales_gato.html');

def animales_perro(retquest):
    contexto = {'mensaje': 'Pagina de perros'}
    return render(retquest, 'animales_perro.html');

def perros(retquest):
    contexto = {'mensaje': 'Pagina de perros'}
    return render(retquest, 'perros.html');

def gatos(retquest):
    contexto = {'mensaje': 'Pagina de gatos'}
    return render(retquest, 'gatos.html');