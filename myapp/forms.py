from django import forms
from django.forms import ModelForm
from .models import Usuario 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class newUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit = True):
        user = super(newUserForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit: 
            user.save()
        return user


#class MyForm(ModelForm):
    
 #   class Meta:
  #      model = Usuario
   #     fields = ['email', 'password']

