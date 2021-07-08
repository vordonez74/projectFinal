from django import forms
from .models import Productos, Categorias, Carrito


class FormProductosCustom(forms.ModelForm):
    # campos del modelo
    class Meta:
        model = Productos
        fields = ('titulo', 'Imagen', 'descripcion', 'precio', 'Categorias')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'estilo_titulo'}),
            'Imagen': forms.TextInput(attrs={'class': 'estilo_Imagen'}),
            'descripcion': forms.TextInput(attrs={'class': 'estilo_descripcion'}),
            'precio': forms.TextInput(attrs={'class': 'estilo_precio'}),
            'Categorias': forms.TextInput(attrs={'class': 'estilo_Categorias'}),
        }


# class FormCategoriasCustom(forms.ModelForm):
    # campos del modelo
#    class Meta:
#        model = Categorias
#        fields = ('descripcion')
#        widgets = {
#            'descripcion': forms.TextInput(attrs={'class': 'estilo_descripcion'}),
#        }


# class FormCarritoCustom(forms.ModelForm):
    # campos del modelo
#    class Meta:
#        model = Carrito
#        fields = ('usuario', 'listaProductos', 'totalCarrito')
#        widgets = {
#            'usuario': forms.TextInput(attrs={'class': 'estilo_usuario'}),
#            'listaProductos': forms.TextInput(attrs={'class': 'estilo_listaProductos'}),
#            'totalCarrito': forms.TextInput(attrs={'class': 'estilo_totalCarrito'}),
#        }
