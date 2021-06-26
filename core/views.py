from django.shortcuts import redirect, render
from .models import Juego
from .forms import JuegoForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    juegos = Juego.objects.all()
    datos = {
        'juegos': juegos
    }
    return render(request, 'core/index.html', datos)

def contacto(request):
    return render(request, 'core/contacto.html')

def logoutpage(request):
    logout(request)
    return redirect('index')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
    context = {}
    return render(request, 'core/login.html', context)

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    return render(request, 'core/registro.html')

def gamepage(request, pk):
    juego = Juego.objects.get(id_juego=pk)
    datos = {
        'juego': juego
    }

    return render(request, 'core/gamepage.html', datos)

def paneladmin(request):
    juegos = Juego.objects.all()
    datos = {
        'juegos': juegos
    }
    return render(request, 'core/paneladmin.html', datos)

def add_game(request):
    if request.method == 'POST':
        form_add = JuegoForm(request.POST, request.FILES)
        if form_add.is_valid:
            form_add.save()
            return redirect(paneladmin)
    else:
        datos = {
            'form': JuegoForm()
        }
        return render(request, 'core/add_game.html', datos)

def edit_game(request, pk):
    juego = Juego.objects.get(id_juego=pk)

    if request.method == 'POST':
        form_edit = JuegoForm(data=request.POST, instance=juego)
        if form_edit.is_valid:
            form_edit.save()
            return redirect(paneladmin)
    else:
        datos = {
            'form': JuegoForm(instance=juego)
        }
        return render(request, 'core/edit_game.html', datos)

def delete_game(request, pk):
    juego = Juego.objects.get(id_juego=pk)
    juego.delete()
    return redirect(paneladmin)