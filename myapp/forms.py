from django import forms


class MyForm(forms.Form):
    nombre = forms.CharField(label = 'Introduce tu nombre', max_length = 100)
    email = forms.EmailField(label = 'Introduce tu email', max_length = 100)