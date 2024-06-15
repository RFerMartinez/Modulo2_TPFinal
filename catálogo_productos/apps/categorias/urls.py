from django.urls import path
from . import views

app_name = "categorias"

urlpatterns = [
    path('listar-categorias/', views.ListarCategorias.as_view(), name='listar_categorias'),
    path('crear-categoria/', views.CrearCategoria.as_view(), name='crear_categoria'),
    path('editar-categoria/<int:pk>/', views.EditarCategoria.as_view(), name='editar_categoria'),
    path('eliminar-categoria/<int:pk>/', views.EliminarCategoria.as_view(), name='eliminar_categoria'),
]
