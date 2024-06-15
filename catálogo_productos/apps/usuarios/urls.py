from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('listar-usuarios/', views.ListarUsuarios.as_view(), name='listar_usuarios'),
]