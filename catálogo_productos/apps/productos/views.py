from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import render

from django.urls import reverse_lazy

from .models import Producto
from .forms import ProductoForm

# Create your views here.
def listarProductos(request):
    template="productos/productos.html"
    ctx = {

    }
    return render(request=request, template_name=template, context=ctx)

# LoginRequiredMixin, VerificarPermisos

class ListarProductos(ListView):
    template_name = "productos/productos.html"
    model = Producto
    paginate_by = 2
    context_object_name = "productos"
    
    
    # def get_queryset(self):
    #     return self.model.objects.all().order_by("-fecha")

class CrearProducto(CreateView):
    template_name = "productos/nuevoProducto.html"
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listar')
