#lugares/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Localidad, Jurisdiccion, EnJurisdiccion, Provincia, EnProvincia, Audiencia, EnAudiencia

def index(request):
    return HttpResponse("Ya llegaste hasta el índice de lugares del proyecto Gálvez. ¿Y ahora?")

def lista_localidades(request):
    return render(request, 'lugares/lista_localidades.html', {'localidades': Localidad.objects.all().order_by('nombre')})

def detalle_localidad(request, localidad_id):
    localidad = get_object_or_404(Localidad, pk=localidad_id)
    en_jurisdiccion = EnJurisdiccion.objects.filter(localidad_id=localidad_id)
    return render(request, 'lugares/detalle_localidad.html', {'localidad': localidad, 'en_jurisdiccion': en_jurisdiccion})

def lista_jurisdicciones(request):
    return render(request, 'lugares/lista_jurisdicciones.html', {'jurisdicciones': Jurisdiccion.objects.all().order_by('nombre')})

def detalle_jurisdiccion(request, jurisdiccion_id):
    jurisdiccion = get_object_or_404(Jurisdiccion, pk=jurisdiccion_id)
    en_jurisdiccion = EnJurisdiccion.objects.filter(jurisdiccion_id=jurisdiccion_id).order_by('localidad')
    en_provincia = EnProvincia.objects.filter(jurisdiccion_id=jurisdiccion_id)
    en_audiencia = EnAudiencia.objects.filter(jurisdiccion_id=jurisdiccion_id)
    return render(request, 'lugares/detalle_jurisdiccion.html', {'jurisdiccion': jurisdiccion, 'en_jurisdiccion': en_jurisdiccion, 'en_provincia': en_provincia, 'en_audiencia': en_audiencia})

def lista_provincias(request):
    return render(request, 'lugares/lista_provincias.html', {'provincias': Provincia.objects.all().order_by('nombre')})

def detalle_provincia(request, provincia_id):
    provincia = get_object_or_404(Provincia, pk=provincia_id)
    en_provincia = EnProvincia.objects.filter(provincia_id=provincia_id).order_by('jurisdiccion')
    return render(request, 'lugares/detalle_provincia.html', {'provincia': provincia, 'en_provincia': en_provincia})

def lista_audiencias(request):
    return render(request, 'lugares/lista_audiencias.html', {'audiencias': Audiencia.objects.all().order_by('nombre')})

def detalle_audiencia(request, audiencia_id):
    audiencia = get_object_or_404(Audiencia, pk=audiencia_id)
    en_audiencia = EnAudiencia.objects.filter(audiencia_id=audiencia_id).order_by('jurisdiccion')
    return render(request, 'lugares/detalle_audiencia.html', {'audiencia': audiencia, 'en_audiencia': en_audiencia})

# Buscador escrito por Julien Phalip

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


def buscador_localidad(request):
    if 'q' in request.GET:
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['nombre', 'notas'])
        localidades = Localidad.objects.filter(entry_query).distinct().order_by("nombre")
    return  render(request, 'lugares/buscador_localidad.html', {'query_string': query_string, 'localidades': localidades})

def buscador_jurisdiccion(request):
    if 'q' in request.GET:
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['nombre', 'notas'])
        jurisdicciones = Jurisdiccion.objects.filter(entry_query).distinct().order_by("nombre")
    return  render(request, 'lugares/buscador_jurisdiccion.html', {'query_string': query_string, 'jurisdicciones': jurisdicciones})
