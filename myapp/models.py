from django.db import models

# Create your models here.

# Creacion de la clase Ingrediente
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=20)
    calorias = models.IntegerField
    receta = ForeignKey(Receta, on_delete=models.CASCADE)
    cantidad = ForeignKey(Cantidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
