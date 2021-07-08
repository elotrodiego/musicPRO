from django.urls import path
from .views import apiJuegos, juego
from .loginview import login

urlpatterns = [
    path('juego/', apiJuegos, name="apijuegos"),
    path('juego/<pk>', juego, name="apijuego"),
    path('login/', login, name='apilogin'),
]