from django.urls import path
from . import views

app_name = "categorias"

urlpatterns = [
    path('listar-categorias/', views.ListarCategorias.as_view(), name='listar_categorias'),
]