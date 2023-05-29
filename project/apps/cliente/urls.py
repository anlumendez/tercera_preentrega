from django.urls import path

from .views import index, crear_cliente, prueba_busqueda, crear

# Es necesario este nombre, para ser llamado desde la plantila,
# por ejemplo: {% url 'cliente:index' %}
app_name = "cliente"

urlpatterns = [
    path("", index, name="index"),
    path("crear_cliente/", crear_cliente, name="crear_cliente"),
    path("prueba_busqueda/", prueba_busqueda, name="prueba_busqueda"),
    path("crear/", crear, name="crear"),
]
