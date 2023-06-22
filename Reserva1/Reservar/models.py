from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    rut = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.nombre


class Origen(models.Model):
    ciudadOrigen = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.ciudadOrigen


class Destino(models.Model):
    ciudadDestino = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.ciudadDestino


class Ruta(models.Model):
    ciudadOrigen = models.ForeignKey(Origen, on_delete=models.CASCADE)
    ciudadDestino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    tiempoEstimado = models.CharField(max_length=100)

    def __str__(self):
        return self.ciudadDestino


class Bus(models.Model):
    patente = models.CharField(max_length=50, unique=True)
    cantidadAsientos = models.IntegerField()

    def __str__(self):
        return self.patente


class Asientos(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    estado = models.BooleanField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)


class Reserva(models.Model):
    fechaReserva = models.DateTimeField(null=False)
    cantidadPasajes = models.IntegerField(null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    asiento = models.ForeignKey(Asientos, on_delete=models.CASCADE)

    def __str__(self):
        return self.fechaReserva


class Disponibilidad(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE,
                            related_name='disponibilidades_bus')
    asiento = models.ForeignKey(
        Asientos, on_delete=models.CASCADE, related_name='disponibilidades_asiento')
    ruta = models.ForeignKey(
        Ruta, on_delete=models.CASCADE, related_name='disponibilidades_ruta')
    horario = models.TimeField()
    fecha = models.DateField()
    disponible = models.BooleanField()

    def __str__(self):
        return self.horario


# Create your models here.
