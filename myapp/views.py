from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Receta, Ingrediente, Cantidad, TipoReceta, Usuario
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models.query import QuerySet
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import newUserForm, CantidadRecetaIngredienteModelForm
"""MyForm,"""
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.

# Vista para ver todos los ingredientes

class IngredientesListView(ListView):
    model = Ingrediente
    querySet = Ingrediente.objects.all()
    ordering = ('nombre',)
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
    ordering = ('nombre',)
    template_name = 'listarecetas.html'

class RecetasDetailView(DetailView):
    model = Receta
    template_name = 'detallereceta.html'

class PortadaListView(ListView):
    model = TipoReceta
    QuerySet = TipoReceta.objects.all()
    template_name = 'portada.html'

def register_request(request):
    if request.method == "POST":
        form = newUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(request.POST.get("groups"))
            login(request, user)
            messages.success(request, "Registro correcto")
            return redirect("/myapp/")
        messages.error(request, "Algunos campos del registro son erróneos")
    form = newUserForm()
    return render(request=request, template_name = "registro.html", context ={"register_form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Estas logeado como {username}")
                return redirect("/myapp/")
            else:
               messages.error(request, "Usuario o contraseña incorrecta")  
        else:
            messages.error(request, "Usuario o contraseña incorrecta")
    form = AuthenticationForm()
    return render(request=request, template_name = "login.html", context ={"login_form": form})

def logout_request(request):
    logout(request)
    return redirect("/myapp/")


"""class RecetaForm(CreateView):
    model= Receta
    fields=['nombre', 'descripcion', 'tiempo', 'tipo', 'duracion']
    template_name = 'añadirReceta.html'
    success_url = reverse_lazy('id_port')
 """
  
#Pruebas-----------

class CantidadCreateView(CreateView):
    form_class = CantidadRecetaIngredienteModelForm
    template_name = 'añadirReceta.html'
    
    def form_valid(self, form):
        receta = form['receta'].save()
        ingrediente = form['ingrediente'].save()
        cantidad = form['cantidad'].save(commit=False)
        cantidad.receta = receta
        cantidad.ingrediente = ingrediente
        cantidad.save()
        success_url = reverse_lazy('id_port')
        return redirect("/myapp/")

    
#class LoginForm(CreateView):
#    model=Usuario
 #   fields=['email', 'password']
  #  template_name = 'login.html'
   # success_url = reverse_lazy('id_port')

#class RegistroForm(CreateView):
 #   model=Usuario
  #  fields=['nombre','email', 'password']
   # template_name = 'registro.html'
    #success_url = reverse_lazy('id_port')

# Prueba de comentario


