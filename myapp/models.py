from django.db import models
from enum import Enum

class TipoReceta(Enum):
    D = "Desayuno"
    A = "Aperitivo"
    CO = "Comida"
    M = "Merienda"
    CE = "Cena"

class DuracionReceta(Enum):
    MR = "Muy rapido"
    R = "Rapido"
    M = "Medio"
    L = "Lento"
    ML = "Muy lento"

class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    tiempo = models.IntegerField()
    tipo = models.CharField(
        choices=[(tag, tag.value) for tag in TipoReceta]
    )
    duracion = models.CharField(
        choices=[(tag, tag.value) for tag in DuracionReceta]
    )
    def __str__(self):
        return self.nombre


# Creacion de la clase Ingrediente
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=20)
    calorias = models.IntegerField()
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    cantidad = models.ForeignKey(Cantidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Cantidad(models.Model):
    cantidad = models.IntegerField(default=0)
    unidad = models.CharField(max_length=40)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
