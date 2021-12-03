from django import forms
from django.forms.widgets import PasswordInput


class MyForm(forms.Form):
    nombre = forms.CharField(label = 'Introduce tu nombre', max_length = 100)
    email = forms.EmailField(label = 'Introduce tu email', max_length = 100)
    password = forms.CharField(label = 'Introduce contraseña', widget=PasswordInput(), max_length=100)