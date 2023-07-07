from django import forms
from datetime import date
from .models import Bus, Ruta, Ciudades, Asientos, Horarios_buses, Cliente, Reserva


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
        label='Tiempo estimado:', widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Ruta
        fields = ['ciudadO', 'ciudadD', 'tiempoEstimado']


class AsientosForm(forms.ModelForm):

    class Meta:
        model = Asientos
        fields = ['numero', 'bus']
        labels = {'numero': 'Numero de asiento:', 'bus': 'Bus'}


class Horarios_busesForm(forms.ModelForm):
    bus = forms.ModelChoiceField(queryset=Bus.objects.all(), label='Bus:')
    ruta = forms.ModelChoiceField(
        queryset=Ruta.objects.all(), label='Ruta:')
    horario = forms.TimeField(
        label='Horario:', widget=forms.TimeInput(attrs={'type': 'time'}))
    fecha = forms.DateField(
        label='Fecha:', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Horarios_buses
        fields = ['bus', 'ruta', 'horario', 'fecha']


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidoP',
                  'apellidoM', 'email', 'telefono', 'rut']
        labels = {'nombre': 'Nombre:', 'apellidoP': 'Apellido paterno:', 'apellidoM': 'Apellido materno:',
                  'email': 'Email', 'telefono': 'Telefono:', 'rut': 'Rut:'}


class ReservaForm(forms.ModelForm):
    fechaReserva = forms.DateField(
        label='Fecha:', widget=forms.DateInput(attrs={'type': 'date'}))
    horarioReserva = forms.TimeField(
        label='Horario:', widget=forms.TimeInput(attrs={'type': 'time'}))
    ruta = forms.ModelChoiceField(
        queryset=Ruta.objects.all(), label='Ruta:')
    asiento = forms.ModelChoiceField(
        queryset=Asientos.objects.all(), label='Asiento:')

    class Meta:
        model = Reserva
        fields = ['fechaReserva', 'horarioReserva',
                  'ruta', 'asiento']
