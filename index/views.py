from django.shortcuts import render

# Create your views here.


def index(retquest):
    contexto = {'mensaje': 'Pagina de inicio'}
    return render(retquest, 'index.html');