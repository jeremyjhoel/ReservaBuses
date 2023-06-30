from django.contrib import admin
from .models import Cliente, Ruta, Bus, Asientos, Reserva, Disponibilidad, Ciudades, Asientos, Horarios_buses

admin.site.register(Cliente)
admin.site.register(Ruta)
admin.site.register(Bus)
admin.site.register(Asientos)
admin.site.register(Reserva)
admin.site.register(Disponibilidad)
admin.site.register(Ciudades)
admin.site.register(Horarios_buses)

# Register your models here.
