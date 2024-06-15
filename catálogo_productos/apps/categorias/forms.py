from django import forms

from ..productos.models import Categoria

class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = ["nombre"]