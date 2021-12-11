from django import forms
from django.forms import ModelForm
from .models import Usuario, Receta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class newUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "groups")
    
    def save(self, commit = True):
        user = super(newUserForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.group = self.cleaned_data['groups']
        if commit: 
            user.save()
        return user

class MyForm(ModelForm):

    class Meta:
        model = Receta
        fields=['nombre', 'descripcion', 'tiempo', 'tipo', 'duracion']


