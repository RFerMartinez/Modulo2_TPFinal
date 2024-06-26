from urllib.parse import parse_qs, urlencode, urlparse, urlunparse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.usuarios.forms import FormularioRegistroUsuario, FormularioEditarPerfil, FormularioCambiarContraseña

def home(request):
    template="home.html"
    ctx = {

    }
    return render(request=request, template_name=template, context=ctx)

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Ruta a la plantilla que contiene la modal

    def form_valid(self, form):
        # Redireccionar a la URL almacenada en 'next' después del inicio de sesión exitoso
        next_url = self.request.POST.get('next', self.success_url)
        return HttpResponseRedirect(next_url)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                # Redirigir a la URL de referencia sin los parámetros de error
                referer_url = request.META.get('HTTP_REFERER', '/')
                
                # Parsear la URL para eliminar los parámetros antiguos
                parsed_url = urlparse(referer_url)
                query_params = parse_qs(parsed_url.query)

                # Quitar los parámetros antiguos
                query_params.pop('show_login_modal', None)
                query_params.pop('error_message', None)

                # Reconstruir la URL limpia
                new_query_string = urlencode(query_params, doseq=True)
                redirect_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query_string, parsed_url.fragment))

                # Redirigir a la URL limpia
                return redirect(redirect_url or '/')
            else:
                # Obtener la URL de referencia
                referer_url = request.META.get('HTTP_REFERER', '/')

                # Parsear la URL para eliminar parámetros antiguos
                parsed_url = urlparse(referer_url)
                query_params = parse_qs(parsed_url.query)

                # Quitar los parámetros antiguos si existen
                query_params.pop('show_login_modal', None)
                query_params.pop('error_message', None)

                # Añadir los nuevos parámetros de error
                query_params.update({'show_login_modal': '1', 'error_message': 'Usuario o contraseña incorrectos.'})

                # Reconstruir la URL limpia con los nuevos parámetros
                new_query_string = urlencode(query_params, doseq=True)
                redirect_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query_string, parsed_url.fragment))

                # Redirigir a la misma página con los parámetros limpios
                return redirect(redirect_url)
    else:
        form = LoginForm()

    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def registrar(request):
    template_name = "registrar.html"

    form = FormularioRegistroUsuario()

    mensaje = None

    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            mensaje = "Usuario creado correctamente. Puede iniciar sesion"
        else:
            print(f"ERRORES: {form.errors}")
    
    ctx = {
        'form': form,
        'mensajeCorrecto': mensaje,
    }
    return render(request=request, template_name=template_name, context=ctx)

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form_perfil = FormularioEditarPerfil(request.POST, request.FILES, instance=request.user)
        form_password = FormularioCambiarContraseña(request.user, request.POST)
        
        if form_perfil.is_valid():
            form_perfil.save()
            messages.success(request, 'Tu perfil ha sido actualizado con éxito.')
            return redirect('editar_perfil')
        
        if form_password.is_valid():
            user = form_password.save()
            update_session_auth_hash(request, user)  # Mantener la sesión después de cambiar la contraseña
            messages.success(request, 'Tu contraseña ha sido cambiada con éxito.')
            return redirect('editar_perfil')
    else:
        form_perfil = FormularioEditarPerfil(instance=request.user)
        form_password = FormularioCambiarContraseña(request.user)

    context = {
        'form_perfil': form_perfil,
        'form_password': form_password
    }
    return render(request, 'usuarios/editarPerfil.html', context)