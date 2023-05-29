from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def crear_autor(request):
    if request.method == 'POST':
        form = forms.AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html")
    else:
        form = forms.AutorForm()
        context = {"form": form}
        return render(request, "home/crear_autor.html", context)