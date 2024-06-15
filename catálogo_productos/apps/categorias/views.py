from django.shortcuts import render
from django.views.generic.list import ListView

from ..productos.models import Categoria

class ListarCategorias(ListView):
    template_name = "categorias/listarCategorias.html"
    model = Categoria
    paginate_by = 10
    context_object_name = "categorias"
    
    def get_queryset(self):
        return self.model.objects.all().order_by("pk")
