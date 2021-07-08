from rest_framework import  serializers
from core.models import Juego

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = ['id_juego', 'nombre_juego', 'precio_juego']