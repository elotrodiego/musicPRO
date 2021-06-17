from django.shortcuts import render
from .models import Juego
from .forms import JuegoForm


# Create your views here.

def index(request):
    juegos = Juego.objects.all()
    datos = {
        'juegos': juegos
    }
    return render(request, 'core/index.html', datos)

def contacto(request):
    return render(request, 'core/contacto.html')

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    return render(request, 'core/registro.html')

def gamepage(request, pk):
    juego = Juego.objects.get(id_juego=pk)
    datos = {
        'juego': juego
    }

    return render(request, 'core/gamepage.html', datos)
