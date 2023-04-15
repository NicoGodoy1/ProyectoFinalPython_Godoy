from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from AppCelularUsado.models import Producto

class CelularFormulario(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()
    vendido= forms.BooleanField()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()
    imagenCelular = forms.ImageField()

# . 



# .

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido =  forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Conteseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir conteseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

