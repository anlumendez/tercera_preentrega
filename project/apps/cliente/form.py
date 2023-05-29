from django import forms

from .models import Cliente, Pais

class ClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "apellido", "nacimiento", "pais_origen_id"]

class PaisForms(forms.ModelForm):
    class Meta:
        model = Pais
        fields = "__all__"
