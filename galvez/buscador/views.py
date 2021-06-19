#buscador/views.py
from django.shortcuts import render

def buscador(request):
    return render(request, 'buscador/buscador.html')
