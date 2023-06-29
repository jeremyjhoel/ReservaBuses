from django import forms
from .models import Bus, Ruta, Ciudades, Asientos


class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ('patente', 'cantidadAsientos')
        labels = {
            'patente': 'Patente del bus',
            'cantidadAsientos': 'Cantidad de asientos',
        }


class CiudadForm(forms.ModelForm):

    class Meta:
        model = Ciudades
        fields = ('ciudad',)
        labels = {
            'ciudad': 'Ciudad',
        }


class RutaForm(forms.ModelForm):
    ciudadO = forms.ModelChoiceField(queryset=Ciudades.objects.all(
    ), label='Ciudad de origen:')
    ciudadD = forms.ModelChoiceField(queryset=Ciudades.objects.all(
    ), label='Ciudad de destino:')
    tiempoEstimado = forms.TimeField(
        label='Tiempo estimado:')

    class Meta:
        model = Ruta
        fields = ['ciudadO', 'ciudadD', 'tiempoEstimado']


class Asientos(forms.ModelForm):

    class Meta:
        model = Asientos
        fields = ['numero', 'estado', 'bus']
        labels = {'numero': 'Numero de asiento:',
                  'estado': 'Estado', 'bus': 'Bus'}
