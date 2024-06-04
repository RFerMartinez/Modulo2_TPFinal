# Modulo2_TPFinal
***
## Sistema para presentar un catálogo de productos
Dicho sistema permite gestionar productos, se tendrá tres 'usuarios' (usuarios administradores, usuarios registrados y usuarios anónimos).
### Usuarios 'administradores'
Un usuario administrador podrá:
* Crear nuevos productos.
* Editar productos.
* Eliminar productos.
* Crear categorías.
* Editar categorías.
* Eliminar procategoríasductos.
* desactivar productos.
* Listar los usuarios creados y poder diferenciarlos de los administradores
### Usuarios 'registradoes'
Los usuarios que se encuentran registrados podran:
* Iniciar/cerrar Sesion.
* Marcar un producto como favorito, ya sea desde el catálogo o desde el detalles del mismo producto.
* Quitar productos de favoritos.
* Listar a los productos que haya agregado como favoritos.
* Ver su información de perfir. Editar datos personales
### Usuarios 'anónimos'
Los usuarios anónimos podrán:
* Visualizar la lista de productos de la pñagina web.
* Ver detalles de un producto.
* Regsitrarse a al sitio web.

## Instalación
***
Versión de Python: 3.11.3

Clonar repo en una ruta deseada 
```
$ git clone https://github.com/RFerMartinez/Modulo2_TPFinal.git
```

Crear un entorno virtual (para instalar las dependencias del proyecto) 
```
$ python -m venv nombre_del_entornoVirtual
```

Activar el entorno virtual. Estando en el directorio donde se instaló la carpeta del entorno, ejecutar el siguiente comando:
```
$ .\nombre_del_entornoVirtual\Scripts\activate
```

Una vez activado el entorno virtual, 'navegar' hasta llegar al directorio donde se enceuntre el archivo 'requirements.txt'. El cual se enceuntra dentro del proyecto clonado. Ejecutar el siguiente comando:
```
$ pip install -r requirements.txt
```

Estando en la ruta donde se encuentre el archivo 'requirements.txt'. Dirigirse al directorio 'catálogo_productos' y ejecutar el archivo 'manage.py'
```
$ cd catálogo_productos
```
```
$ python manage.py runserver
```
