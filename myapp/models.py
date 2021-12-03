from django.db import models

class TipoReceta(models.Model):
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

class DuracionReceta(models.Model):
    duracion = models.CharField(max_length=50)
    def __str__(self):
        return self.duracion

class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=10000)
    tiempo = models.IntegerField(default = 0)
    tipo = models.ForeignKey(TipoReceta, on_delete=models.CASCADE, default=None)
    duracion = models.ForeignKey(DuracionReceta, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.nombre

# Creacion de la clase Ingrediente
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    calorias = models.IntegerField(default = 0)
    def __str__(self):
        return self.nombre

class Cantidad(models.Model):
    cantidad = models.FloatField(default=0)
    unidad = models.CharField(max_length=40)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, default = None)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, default = None)
    def __str__(self):
        return self.unidad

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre



