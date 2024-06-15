from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from ..productos.models import Categoria
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