from django import forms
from django.forms import ModelForm
from .models import Juego

class JuegoForm(ModelForm):
    class Meta:
        model = Juego
        fields = ['id_juego',
        'imagen_juego',
        'destacado',
        'nombre_juego',
        'desc_juego',
        'precio_juego',
        'desarrollador_juego',
        'editor_juego',
        'fecha_juego',
        'genero_juego',
        'genero_juego2',
        'genero_juego3',
        'genero_juego4',
        'carousel',
        'carousel2',
        'carousel3',
        'carousel4']