from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

# Formulario para poder regsitrar usuario
class FormularioRegistroUsuario(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control1',
        })
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control1',
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control1',
        })
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    password2 = forms.CharField(
        label="Repita contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    imagen = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control1',
        })
    )

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'imagen', 'email']

    def __init__(self, *args, **kwargs):
        super(FormularioRegistroUsuario, self).__init__(*args, *kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repite la contraseña'