from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('listar-paginado/', views.ListarProductos.as_view(), name='listar'),
    path('crear-producto', views.CrearProducto.as_view(), name='crear_producto'),
    path('toggle-favorito/<int:producto_id>/', views.toggle_favorito, name='toggle-favorito'),
    path('lista-favoritos/', views.ListarFavoritos.as_view(), name='lista_favorito'),
    path('editar-producto/<int:pk>/', views.EditarProducto.as_view(), name='editar'),
]

