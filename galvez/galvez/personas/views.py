from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Persona

def index(request):
    return HttpResponse("Ya llegaste hasta el índice de personas del proyecto Gálvez. ¿Y ahora?")

def lista_personas(request):
    return render(request, 'personas/lista_personas.html', {'personas': Persona.objects.all().order_by('ordenar_por_nombre')})

def detalle_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    return render(request, 'personas/detalle_persona.html', {'persona': persona})
