from django.shortcuts import render

def inicio(request):
    return render(request, 'static/inicio.html')

def acerca(request):
    return render(request, 'static/acerca.html')
