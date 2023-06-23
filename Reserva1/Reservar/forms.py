from django import forms
from .models import Bus, Ruta, Destino, Origen


class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ('patente', 'cantidadAsientos')


class DestinoForm(forms.ModelForm):

    class Meta:
        model = Destino
        fields = ('ciudadDestino',)


class OrigenForm(forms.ModelForm):

    class Meta:
        model = Origen
        fields = ('ciudadOrigen',)


class RutaForm(forms.ModelForm):
    ciudadO = forms.ModelChoiceField(queryset=Origen.objects.all())
    ciudadD = forms.ModelChoiceField(queryset=Destino.objects.all())
    tiempoEstimado = forms.TimeField()

    class Meta:
        model = Ruta
        fields = ['ciudadO', 'ciudadD', 'tiempoEstimado']
