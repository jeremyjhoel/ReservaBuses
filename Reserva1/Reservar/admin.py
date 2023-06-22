from django.contrib import admin
from .models import Cliente, Ruta, Bus, Asientos, Reserva, Disponibilidad

admin.site.register(Cliente)
admin.site.register(Ruta)
admin.site.register(Bus)
admin.site.register(Asientos)
admin.site.register(Reserva)
admin.site.register(Disponibilidad)


# Register your models here.
