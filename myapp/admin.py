from django.contrib import admin
from .models import DuracionReceta, Receta, Ingrediente, Cantidad, TipoReceta, Usuario



class CantidadInline(admin.TabularInline):
    model = Cantidad
    extra = 1

class RecetaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Resumen',               {'fields': ['nombre', 'descripcion']}),
        ('Tipo de receta',        {'fields': ['tipo']}),
        ('Tiempo y duracion',     {'fields': ['tiempo', 'duracion'], 'classes': ['collapse']}),
    ]
    inlines = [CantidadInline]
    list_display = ('nombre', 'tipo', 'duracion')

class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'calorias')



admin.site.register(Receta, RecetaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Cantidad)
admin.site.register(TipoReceta)
admin.site.register(DuracionReceta)
admin.site.register(Usuario)
# Register your models here.




