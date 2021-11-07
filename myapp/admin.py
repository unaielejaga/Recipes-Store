from django.contrib import admin
from .models import Receta, Ingrediente, Cantidad

admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(Cantidad)
# Register your models here.
