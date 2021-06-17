from django import forms
from django.forms import ModelForm
from .models import Juego

class JuegoForm(ModelForm):
    class Meta:
        model = Juego
        fields = ['id_juego','nombre_juego']