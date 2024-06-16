
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as views_django
from django.conf import settings
from django.conf.urls.static import static


from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registrar/', views.registrar, name='registrar'),

    # --LOGIN--
    # path('login/', )

    path("productos/", include('apps.productos.urls')),
    path("usuarios/", include('apps.usuarios.urls')),
    path("categorias/", include('apps.categorias.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

