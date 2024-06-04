from django.shortcuts import render

# Create your views here.


def animales_gato(retquest):
    contexto = {'mensaje': 'Pagina de gatos'}
    return render(retquest, 'animales_gato.html');