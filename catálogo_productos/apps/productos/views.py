from django.shortcuts import render

# Create your views here.
def listarProductos(request):
    template="productos/productos.html"
    ctx = {

    }
    return render(request=request, template_name=template, context=ctx)