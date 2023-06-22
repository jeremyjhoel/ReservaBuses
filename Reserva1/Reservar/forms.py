from django import forms
from .models import Bus, Ruta, Destino


class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ('patente', 'cantidadAsientos')


class DestinoForm(forms.ModelForm):

    class Meta:
        model = Destino
        fields = ('ciudadDestino',)


class RutaForm(forms.ModelForm):

    class Meta:
        model = Ruta
        fields = ('ciudadOrigen', 'ciudadDestino', 'tiempoEstimado')
