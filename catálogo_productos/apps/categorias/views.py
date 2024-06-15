from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from ..productos.models import Categoria, Producto
from .forms import CategoriaForm

class ListarCategorias(ListView):
    template_name = "categorias/listarCategorias.html"
    model = Categoria
    paginate_by = 10
    context_object_name = "categorias"
    
    def get_queryset(self):
        return self.model.objects.all().order_by("pk")

class CrearCategoria(CreateView):
    template_name = "categorias/nuevaCategoria.html"
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias:listar_categorias')

class EditarCategoria(UpdateView):
    template_name = "categorias/editarCategoria.html"
    model = Categoria
    form_class = CategoriaForm
    success_url = reverse_lazy('categorias:listar_categorias')

class EliminarCategoria(DeleteView):
    template_name = "categorias/eliminarCategoria.html"
    model = Categoria
    success_url = reverse_lazy('categorias:listar_categorias')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtiene los productos asociados a la categoría que se está eliminando
        context['productos_asociados'] = Producto.objects.filter(categoria=self.object)
        return context

    def eliminar(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Manejar lo que sucede con los productos asociados.
        productos_asociados = Producto.objects.filter(categoria=self.object)
        
        # Eliminar productos asociados
        productos_asociados.eliminar()

        return super().eliminar(request, *args, **kwargs)