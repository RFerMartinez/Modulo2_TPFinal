from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path('listar-paginado/', views.ListarProductos.as_view(), name='listar'),
    path('listar-productos-admin/', views.ListarProductosAdmin.as_view(), name='listar_admin'),

    path('crear-producto', views.CrearProducto.as_view(), name='crear_producto'),
    path('crear-producto-Tolist', views.CrearProductoTolist.as_view(), name='crear_producto_tolist'),

    path('editar-producto/<int:pk>/', views.EditarProducto.as_view(), name='editar'),
    path('editar-producto-toList/<int:pk>/', views.EditarProductoTolist.as_view(), name='editar_tolist'),

    path('eliminar/<int:pk>/', views.EliminarProducto.as_view(), name='eliminar'),
    path('eliminar-Tolist/<int:pk>/', views.EliminarProductoTolist.as_view(), name='eliminar_tolist'),

    path('lista-favoritos/', views.ListarFavoritos.as_view(), name='lista_favorito'),

    path('toggle-favorito/<int:producto_id>/', views.toggle_favorito, name='toggle-favorito'),

    path('detalles/<int:pk>/', views.mostrarDetalles, name='mostrar_detalle'),
]

