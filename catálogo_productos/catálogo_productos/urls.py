
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as views_django


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
]

