from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

from .models import Producto, Favorito
from .forms import ProductoForm

class ListarProductos(ListView):
    template_name = "productos/productos.html"
    model = Producto
    paginate_by = 10
    context_object_name = "productos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Obtener los favoritos del usuario actual
            favoritos = Favorito.objects.filter(usuario=self.request.user)
            # Extraer solo los IDs de los productos favoritos
            favoritos_ids = list(favoritos.values_list('producto_id', flat=True))
            context['favoritos_ids'] = favoritos_ids
        return context
    
    def get_queryset(self):
        return Producto.objects.all().order_by('nombre')

class CrearProducto(LoginRequiredMixin, CreateView):
    template_name = "productos/nuevoProducto.html"
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listar')

class CrearProductoTolist(LoginRequiredMixin, CreateView):
    template_name = "productos/nuevoProducto.html"
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listar_admin')

class EditarProducto(UpdateView):
    template_name = "productos/editarProducto.html"
    model = Producto
    form_class = ProductoForm #Tiene el mismo modelo, ya que los campos que se usan para crear, también se usan para editar
    success_url = reverse_lazy('productos:listar')

class EditarProductoTolist(UpdateView):
    template_name = "productos/editarProducto.html"
    model = Producto
    form_class = ProductoForm #Tiene el mismo modelo, ya que los campos que se usan para crear, también se usan para editar
    success_url = reverse_lazy('productos:listar_admin')

def toggle_favorito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST' and request.user.is_authenticated:
        # Intentar obtener un objeto Favorito existente
        favorito, created = Favorito.objects.get_or_create(usuario=request.user, producto=producto)
        if not created:
            # Si ya existe, se elimina para "desfavorecer" el producto
            favorito.delete()
            es_favorito = False
        else:
            # Si se creó, significa que ahora es favorito
            es_favorito = True

        # Devolver el nuevo estado del favorito
        return JsonResponse({'favorito': es_favorito})
    else:
        return JsonResponse({'error': 'No se pudo realizar la acción'})

class ListarFavoritos(LoginRequiredMixin, ListView):
    template_name = "productos/listaFavoritos.html"  # Ruta al template específico para mostrar favoritos
    model = Producto  # Modelo que se listará
    paginate_by = 10  # Número de elementos por página
    context_object_name = "productos"  # Nombre del contexto para acceder a los productos en la plantilla

    def get_queryset(self):
        # Filtrar los productos que están en la lista de favoritos del usuario logueado
        user = self.request.user
        favoritos = Favorito.objects.filter(usuario=user).values_list('producto_id', flat=True)
        return Producto.objects.filter(id__in=favoritos)

    def get_context_data(self, **kwargs):
        # Agregar datos adicionales al contexto si es necesario
        context = super().get_context_data(**kwargs)
        context['es_favorito'] = True  # Ejemplo de cómo puedes agregar más datos al contexto
        return context

class EliminarProducto(View):
    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return redirect('productos:listar')

class EliminarProductoTolist(View):
    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return redirect('productos:listar_admin')

class ListarProductosAdmin(LoginRequiredMixin, ListView):
    template_name = "productos/admin_listaProductos.html"
    model = Producto
    paginate_by = 15
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.all().order_by('nombre')

def mostrarDetalles(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    # Obtener los favoritos del usuario actual
    if request.user.is_authenticated:
        favoritos = Favorito.objects.filter(usuario=request.user)
        favoritos_ids = list(favoritos.values_list('producto_id', flat=True))
    else:
        favoritos_ids = []

    context = {
        'productos': producto,
        'favoritos_ids': favoritos_ids,
    }
    return render(request, 'productos/mostrarDetalle.html', context)

def buscarProductos(request):
    query = request.GET.get('query')

    if query:
        # Realizar la búsqueda en base al campo 'nombre' del modelo Producto
        resultados = Producto.objects.filter(nombre__icontains=query)
        context = {
            'query': query,
            'resultados': resultados
        }
        return render(request, 'productos/buscarProductos.html', context)
    else:
        # Si no hay consulta válida, redirigir a la página que lista todos los productos
        return redirect('productos:listar')  # Ajusta 'productos:listar' con la URL de tu vista que lista todos los productos