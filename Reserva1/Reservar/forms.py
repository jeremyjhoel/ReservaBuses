from django import forms
from .models import Bus, Ruta, Ciudades, Asientos, Disponibilidad


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


class AsientosForm(forms.ModelForm):

    class Meta:
        model = Asientos
        fields = ['numero', 'bus']
        labels = {'numero': 'Numero de asiento:', 'bus': 'Bus'}


class DisponibilidadForm(forms.ModelForm):
    bus = forms.ModelChoiceField(queryset=Bus.objects.all(), label='Bus:')
    ruta = forms.ModelChoiceField(queryset=Ruta.objects.all(), label='Ruta:')
    horario = forms.TimeField(label='Horario:')
    fecha = forms.DateField(label='Fecha:')
    disponible = forms.BooleanField(label='Disponibilidad:')

    class Meta:
        model = Disponibilidad
        fields = ['bus', 'ruta', 'horario', 'fecha', 'disponible']
