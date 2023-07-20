from django import forms
from datetime import date
from .models import Bus, Ruta, Ciudades, Asientos, Horarios_buses, Cliente, Reserva, Disponibilidad, Horario, Fecha


class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ('patente', 'cantidadAsientos')
        labels = {
            'patente': 'Patente del bus',
            'cantidadAsientos': 'Cantidad de asientos',
        }


class HorarioForm(forms.ModelForm):

    horario = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Horario
        fields = ('horario',)
        labels = {'horario': 'Horario:'}


class FechaForm(forms.ModelForm):

    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Fecha
        fields = ('fecha',)
        labels = {'fecha': 'Fecha:'}


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
    ciudadO = forms.ModelChoiceField(
        queryset=Ciudades.objects.all(), label='Ciudad de origen:')
    ciudadD = forms.ModelChoiceField(
        queryset=Ciudades.objects.all(), label='Ciudad de destino:')
    fecha = forms.ModelChoiceField(queryset=Fecha.objects.all(),
                                   label='Fecha:')
    horario = forms.ModelChoiceField(queryset=Horario.objects.all(),
                                     label='Horario:')

    class Meta:
        model = Horarios_buses
        fields = ['bus', 'ciudadO', 'ciudadD', 'horario', 'fecha']


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellidoP',
                  'apellidoM', 'email', 'telefono', 'rut']
        labels = {'nombre': 'Nombre:', 'apellidoP': 'Apellido paterno:', 'apellidoM': 'Apellido materno:',
                  'email': 'Email', 'telefono': 'Telefono:', 'rut': 'Rut:'}


class ReservaForm(forms.ModelForm):
    fecha = forms.ModelChoiceField(queryset=Fecha.objects.all(),
                                   label='Fecha:')
    horario = forms.ModelChoiceField(queryset=Horario.objects.all(),
                                     label='Horario:')
    ciudadO = forms.ModelChoiceField(
        queryset=Ciudades.objects.all(), label='Ciudad de origen:')
    ciudadD = forms.ModelChoiceField(
        queryset=Ciudades.objects.all(), label='Ciudad de destino:')

    class Meta:
        model = Reserva
        fields = ['fecha', 'horario', 'ciudadO', 'ciudadD']
