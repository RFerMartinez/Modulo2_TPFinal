from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Usuario
from ..productos.models import Categoria

# Función para listar usuarios. view solo para perfiles 'admin'
class ListarUsuarios(ListView):
    template_name = "usuarios/listarTodos.html"
    model = Usuario

    # Para paginar los dato que se muestran
    paginate_by = 10

    # Redefinir el nombre del contexto, en vez de que se llame 'object_list', se llamará 'usuarios'
    context_object_name = "usuarios"
    
    #REDEFINIR LA FUNCION PARA MOSTRAR LO DEL CONTEXT
    def get_context_data(self, **kwards):
        # lo siguiente le pide la información que ya tiene en el context, para luego agregar información adicional
        ctx = super(ListarUsuarios, self).get_context_data(**kwards)
        # ctx['icono'] = "o"
        # Ahora tiene que retornar el contexto actualizado
        return ctx
    
    def get_queryset(self):
        # Por defecto la consulta que realiza un 'ListView' es un .all() y se lo pasa via 'context'
        # luego en el .html se ocupa lo necesario
        return self.model.objects.all().order_by("pk")

class ListarCategorias(ListView):
    template_name = "categorias/listarCategorias.html"
    model = Categoria
    paginate_by = 10
    context_object_name = "categorias"
    
    def get_queryset(self):
        return self.model.objects.all().order_by("pk")
