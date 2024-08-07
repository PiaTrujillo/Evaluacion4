from django import forms
from django.forms import ModelForm 
from .models import Producto

class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['sku','dv','nombre','primer_apellido','segundo_apellido','descripcion','categoria','precio','stock']