from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

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
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a la página desde donde se hizo el login
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            # Mostrar mensaje de error en la modal
            return render(request, 'base.html', {'error_message': 'Usuario o contraseña incorrectos.'})
    else:
        # Si se accede al login por GET (no debería pasar por la modal directamente)
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')