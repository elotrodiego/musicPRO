from django.urls import path
from .views import apiJuegos, juego
from .loginview import login

urlpatterns = [
    path('juego/', apiJuegos, name="juegos"),
    path('juego/<pk>', juego, name="juego"),
    path('login/', login, name='login'),
]