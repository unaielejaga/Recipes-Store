from django.contrib import admin
from .models import DuracionReceta, Receta, Ingrediente, Cantidad, TipoReceta

admin.site.register(Receta)
admin.site.register(Ingrediente)
admin.site.register(Cantidad)
admin.site.register(TipoReceta)
admin.site.register(DuracionReceta)
# Register your models here.
