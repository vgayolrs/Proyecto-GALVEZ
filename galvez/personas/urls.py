from django.urls import path

from . import views

app_name = 'personas'
urlpatterns = [
    path('', views.index, name='index'),
    path('lista_personas/', views.lista_personas, name='lista_personas'),
    path('<int:persona_id>/', views.detalle_persona, name='detalle_persona'),
    path('buscador_persona/', views.buscador_persona, name='buscador_persona'),
]
