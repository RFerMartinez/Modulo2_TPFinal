from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('listar-usuarios/', views.ListarUsuarios.as_view(), name='listar_usuarios'),
    path('listar-categorias/', views.ListarCategorias.as_view(), name='listar_categorias'),
]