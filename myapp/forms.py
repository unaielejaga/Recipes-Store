from django import forms
from django.forms import ModelForm
from .models import Usuario 
 

class MyForm(ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'password']

