from django import forms

class CelularFormulario(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()
    vendido= forms.BooleanField()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField()
    apellido =  forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
