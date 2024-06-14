from django.contrib import admin

from .models import Producto, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

admin.site.register(Producto, ProductoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]

admin.site.register(Categoria, CategoriaAdmin)