from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Horario(models.Model):
    horario = models.TimeField()

    def __str__(self):
        return str(self.horario)


class Fecha(models.Model):
    fecha = models.DateField()

    def __str__(self):
        return str(self.fecha)


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellidoP = models.CharField(max_length=100, null=False)
    apellidoM = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=20, blank=True)
    rut = models.CharField(max_length=200, null=False)

    def __str__(self):
        persona = str(self.nombre) + " " + self.apellidoP + \
            " " + str(self.apellidoM)
        return persona


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


class Horarios_buses(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE,
                            related_name='Horarios_buses_bus')
    ciudadO = models.ForeignKey(
        Ciudades, related_name='Horarios_buses_origen', on_delete=models.CASCADE)
    ciudadD = models.ForeignKey(
        Ciudades, related_name='Horarios_buses_destino', on_delete=models.CASCADE)
    horario = models.ForeignKey(
        Horario, on_delete=models.CASCADE, related_name='Horarios_buses_horario')
    fecha = models.ForeignKey(
        Fecha, on_delete=models.CASCADE, related_name='Horarios_buses_fecha')

    def __str__(self):
        return str(self.horario)


class Disponibilidad(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE,
                            related_name='disponibilidades_bus')
    asiento = models.ForeignKey(
        Asientos, on_delete=models.CASCADE, related_name='disponibilidades_asiento')
    ciudadO = models.ForeignKey(
        Ciudades, related_name='disponibilidades_origen', on_delete=models.CASCADE)
    ciudadD = models.ForeignKey(
        Ciudades, related_name='disponibilidades_destino', on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    horario = models.ForeignKey(
        Horario, on_delete=models.CASCADE, related_name='disponibilidades_horario')
    fecha = models.ForeignKey(
        Fecha, on_delete=models.CASCADE, related_name='disponibilidades_fecha')
    disponible = models.BooleanField()

    def __str__(self):
        if self.disponible:
            ocupacion = "Desocupado"
        else:
            ocupacion = "Ocupado"
        return ocupacion


class Reserva(models.Model):
    fecha = models.ForeignKey(
        Fecha, on_delete=models.CASCADE, related_name='reservas_fecha')
    horario = models.ForeignKey(
        Horario, on_delete=models.CASCADE, related_name='reservas_horario')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ciudadO = models.ForeignKey(
        Ciudades, related_name='reservas_origen', on_delete=models.CASCADE)
    ciudadD = models.ForeignKey(
        Ciudades, related_name='reservas_destino', on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    asiento = models.ForeignKey(Asientos, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fecha)


# Create your models here.
