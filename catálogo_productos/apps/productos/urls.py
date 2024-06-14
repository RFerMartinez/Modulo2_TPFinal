from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('listar-paginado/', views.ListarProductos.as_view(), name='listar'),
    path('crear-producto', views.CrearProducto.as_view(), name='crear_producto'),
    path('agregar-favorito/<int:producto_id>/', views.agregar_favorito, name='agregar_favorito'),
    path('lista-favoritos/', views.ListarFavoritos.as_view(), name='lista_favorito'),
]
