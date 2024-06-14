from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'activo']

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del producto'
                }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ingrese la descripción del producto'
                }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
                }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio del producto'
                }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
                }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].empty_label = "Seleccione una categoría"
        self.fields['activo'].label = "Activo"

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo.")
        return precio
