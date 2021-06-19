from django.urls import path

from . import views

app_name = 'lugares'
urlpatterns = [
    path('', views.index, name='index'),
    path('lista_localidades/', views.lista_localidades, name='lista_localidades'),
    path('<int:localidad_id>/', views.detalle_localidad, name='detalle_localidad'),
    path('lista_jurisdicciones/', views.lista_jurisdicciones, name='lista_jurisdicciones'),
    path('detalle_jurisdiccion/<int:jurisdiccion_id>/', views.detalle_jurisdiccion, name='detalle_jurisdiccion'),
    path('lista_provincias/', views.lista_provincias, name='lista_provincias'),
    path('detalle_provincia/<int:provincia_id>/', views.detalle_provincia, name='detalle_provincia'),
    path('lista_audiencias/', views.lista_audiencias, name='lista_audiencias'),
    path('detalle_audiencia/<int:audiencia_id>/', views.detalle_audiencia, name='detalle_audiencia'),
    path('buscador_localidad/', views.buscador_localidad, name='buscador_localidad'),
    path('buscador_jurisdiccion/', views.buscador_jurisdiccion, name='buscador_jurisdiccion'),
]
