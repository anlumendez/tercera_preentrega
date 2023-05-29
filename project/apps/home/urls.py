from django.urls import path

from .views import index, crear_autor

app_name = "home"

urlpatterns = [
    path("", index, name="index"),
    path("crear_autor", crear_autor, name="crear_autor"),
]