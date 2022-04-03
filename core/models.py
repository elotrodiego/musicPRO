from django.db import models
from django.db.models.fields import IntegerField

#MUSICPRO

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name="id producto")
    nombre_producto = models.CharField(max_length=128, verbose_name="nombre producto")
    tipo_producto = models.CharField(max_length=128, verbose_name="tipo producto")
    marca_producto = models.CharField(max_length=128, verbose_name="marca producto")
    desc_producto = models.CharField(max_length=700, verbose_name="descripcion producto", default="none")
    precio_producto = models.IntegerField(verbose_name="precio producto")
    imagen_producto = models.ImageField(verbose_name="imagen producto", default='static/core/img/default.png', upload_to='core')
    carousel = models.ImageField(verbose_name="carousel1", default='/core/default.jpg', upload_to='core')
    carousel2 = models.ImageField(verbose_name="carousel2", default='/core/default.jpg', upload_to='core')
    carousel3 = models.ImageField(verbose_name="carousel3", default='core/default.jpg', upload_to='core')
    carousel4 = models.ImageField(verbose_name="carousel4", default='core/default.jpg', upload_to='core')


# NOTSTEAM

# Create your models here.
class Genero(models.Model):
    id_genero = models.IntegerField(primary_key=True, verbose_name="id del genero")
    nombre_genero = models.CharField(max_length=128, verbose_name="nombre del genero")
    def __str__(self):
        return self.nombre_genero

class Desarrollador(models.Model):
    id_desarrollador = models.IntegerField(primary_key=True, verbose_name="id del desarrollador")
    nombre_desarrollador = models.CharField(max_length=128, verbose_name="nombre del desarrollador")
    def __str__(self):
        return self.nombre_desarrollador
    class Meta:
        verbose_name_plural = "Desarrolladores" # Cambiar el nombre plural

class Editor(models.Model):
    id_editor = models.IntegerField(primary_key=True, verbose_name="id del editor")
    nombre_editor = models.CharField(max_length=128, verbose_name="nombre del editor")
    def __str__(self):
        return self.nombre_editor
    class Meta:
        verbose_name_plural = "Editores" # Cambiar el nombre plural

class Juego(models.Model):
    id_juego = models.IntegerField(primary_key=True, verbose_name="id del juego")
    destacado = models.BooleanField(verbose_name="juego destacado", default=False)
    nombre_juego = models.CharField(max_length=128, verbose_name="nombre del juego")
    desc_juego = models.CharField(max_length=700, verbose_name="descripcion del juego", default="none")
    imagen_juego = models.ImageField(verbose_name="imagen del juego", default='static/core/img/default.png', upload_to='core')
    precio_juego = models.IntegerField(verbose_name="precio del juego")
    ventas_juego = models.IntegerField(verbose_name="ventas del juego", default=0)
    desarrollador_juego = models.ForeignKey(Desarrollador, on_delete=models.CASCADE, null=True)
    editor_juego = models.ForeignKey(Editor, on_delete=models.CASCADE, null=True)
    fecha_juego = models.DateField(verbose_name="fecha de lanzamiento", null=True, default="2020-01-01")
    genero_juego = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name="genero1", null=True, blank=True)
    genero_juego2 = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name="genero2", null=True, blank=True)
    genero_juego3 = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name="genero3", null=True, blank=True)
    genero_juego4 = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name="genero4", null=True, blank=True)
    carousel = models.ImageField(verbose_name="carousel1", default='/core/default.jpg', upload_to='core')
    carousel2 = models.ImageField(verbose_name="carousel2", default='/core/default.jpg', upload_to='core')
    carousel3 = models.ImageField(verbose_name="carousel3", default='core/default.jpg', upload_to='core')
    carousel4 = models.ImageField(verbose_name="carousel4", default='core/default.jpg', upload_to='core')
    def __str__(self):
        return self.nombre_juego

