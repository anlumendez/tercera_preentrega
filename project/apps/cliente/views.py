import formatter
from django.shortcuts import render, redirect

from .models import Cliente, Pais


def index(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    return render(request, "cliente/index.html", contexto)

def crear_cliente(request):
    from datetime import date
    #crear instancias de paises
    p1 = Pais.objects.create(nombre = "mexico")
    p2 = Pais.objects.create(nombre = "colombia")
    p3 = Pais.objects.create(nombre = "uruguay")
    p4 = Pais.objects.create(nombre = "brasil")

    # Crear clientes
    Cliente.objects.create(nombre= "lucy", apellido ="mendez", nacimiento = date(2015,1,1), pais_origen_id= p1)
    Cliente.objects.create(nombre= "lu", apellido ="mendez", nacimiento = date(200,1,1), pais_origen_id= p2)
    Cliente.objects.create(nombre= "ana", apellido ="mendez", nacimiento = date(115,1,1), pais_origen_id= p3)
    Cliente.objects.create(nombre= "lucia", apellido ="mendez", nacimiento = date(2015,1,1), pais_origen_id= None)

    # return render(request, "cliente/index.html")
    return redirect("cliente:index")

def prueba_busqueda(request):
    from datetime import date
    contexto = {}
    # Busqueda por nombre
    clientes_nombre = Cliente.objects.filter(nombre__contains="lu")
    contexto ["clientes_nombre"] = clientes_nombre

    #Busqueda por fecha de nacimiento
    clientes_nacimiento = Cliente.objects.filter(nacimiento__gte=date(2000,1,1))
    contexto ["clientes_nacimiento"] = clientes_nacimiento

    #Busqieda por pais
    clientes_pais = Cliente.objects.filter(pais_origen_id=None)
    contexto ["clientes_pais"] = clientes_pais

    return render(request, "cliente/resultado.html", contexto)


def crear(request):
    from .form import ClienteForms

    if request.method == "POST":
        form = ClienteForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:index")
    else:
        form = ClienteForms()

    return render(request, "cliente/crear.html", {'form': form})