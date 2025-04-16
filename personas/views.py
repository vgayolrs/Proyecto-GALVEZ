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

import re

from django.db.models import Q

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
        
        '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
        
        '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def buscador_persona(request):
    if 'q' in request.GET:
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['nombre', 'notas'])
        personas = Persona.objects.filter(entry_query).distinct().order_by("ordenar_por_nombre")
    return  render(request, 'personas/buscador_persona.html', {'query_string': query_string, 'personas': personas})
