from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    # path('listar/', views.listarProductos, name='listar'),
    path('listar-paginado/', views.ListarProductos.as_view(), name='listar'),
    path('crear-producto', views.CrearProducto.as_view(), name='crear_producto'),
]
