from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellidoP = models.CharField(max_length=100, null=False)
    apellidoM = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    rut = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.nombre


class Ciudades(models.Model):
    ciudad = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.ciudad


class Ruta(models.Model):
    ciudadO = models.ForeignKey(
        Ciudades, related_name='rutas_origen', on_delete=models.CASCADE)
    ciudadD = models.ForeignKey(
        Ciudades, related_name='rutas_destino', on_delete=models.CASCADE)
    tiempoEstimado = models.TimeField(verbose_name='Tiempo estimado')

    def __str__(self):
        return self.ciudadD.ciudad


class Bus(models.Model):
    patente = models.CharField(max_length=50, unique=True)
    cantidadAsientos = models.IntegerField()

    def __str__(self):
        return self.patente


class Asientos(models.Model):
    numero = models.IntegerField(blank=True, null=True)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.numero)


class Reserva(models.Model):
    fechaReserva = models.DateTimeField(null=False)
    cantidadPasajes = models.IntegerField(null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    asiento = models.ForeignKey(Asientos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fechaReserva)


class Horarios_buses(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE,
                            related_name='Horarios_buses_bus')
    ruta = models.ForeignKey(
        Ruta, on_delete=models.CASCADE, related_name='Horarios_buses_ruta')
    horario = models.TimeField()
    fecha = models.DateField()

    def __str__(self):
        return str(self.horario)


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
        return str(self.horario)

# Create your models here.
