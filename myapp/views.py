from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Receta, Ingrediente, Cantidad, TipoReceta
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models.query import QuerySet
# Create your views here.

# Vista para ver todos los ingredientes

class IngredientesListView(ListView):
    model = Ingrediente
    querySet = Ingrediente.objects.all()
    template_name = 'listaIngredientes.html'

class IngredientesDetailView(DetailView):
    model = Ingrediente
    template_name = 'detalleIngrediente.html'
    
class TiposListView(ListView):
    model = TipoReceta
    querySet = TipoReceta.objects.all()
    template_name = 'listaTipos.html'
    
class TiposDetailView(DetailView):
    model = TipoReceta
    template_name = 'detalleTipos.html'

class RecetasListView(ListView):
    model = Receta
    querySet = Receta.objects.all()
    template_name = 'listarecetas.html'

class RecetasDetailView(DetailView):
    model = Receta
    template_name = 'detallereceta.html'

class PortadaListView(ListView):
    model = TipoReceta
    QuerySet = TipoReceta.objects.all()
    template_name = 'portada.html'
