from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Ya llegaste hasta el índice de personas del proyecto Gálvez. ¿Y ahora?")
