from django.shortcuts import render

# Create your views here.

def index(retquest):
    contexto = {'mensaje': 'Hola Mundo'}
    return render(retquest, 'index.html');