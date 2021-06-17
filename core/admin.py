from django.contrib import admin
from .models import Usuarios, Genero, Juego, Desarrollador, Editor

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Genero)
admin.site.register(Juego)
admin.site.register(Desarrollador)
admin.site.register(Editor)