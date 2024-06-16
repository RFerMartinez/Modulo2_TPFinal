from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

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

class FormularioEditarPerfil(UserChangeForm):
    password = None  # Excluir el campo de la contraseña del formulario principal

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'imagen']  # Puedes incluir otros campos si lo necesitas

    def __init__(self, *args, **kwargs):
        super(FormularioEditarPerfil, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['imagen'].widget.attrs['class'] = 'form-control'

class FormularioCambiarContraseña(PasswordChangeForm):
    old_password = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )

    def __init__(self, *args, **kwargs):
        super(FormularioCambiarContraseña, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['placeholder'] = 'Contraseña actual'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Nueva contraseña'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirma nueva contraseña'