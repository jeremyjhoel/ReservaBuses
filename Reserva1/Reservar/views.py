from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Cliente, Bus, Ruta, Ciudades, Asientos, Horarios_buses, Disponibilidad, Reserva
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BusForm, RutaForm, CiudadForm, Horarios_busesForm, ClienteForm, ReservaForm
from django.urls import reverse_lazy
from datetime import date


def index(request):

    return render(request, 'index.html')


def rutaLista(request):
    rutas = Ruta.objects.all()
    return render(request, 'rutas/ruta_list.html', {'rutas': rutas})


def rutaCreacion(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        rutas = form.save(commit=False)
        if form.is_valid():
            print(rutas.ciudadO.ciudad, "esta es la que entra")

            if rutas.ciudadO.ciudad == rutas.ciudadD.ciudad:
                messages.error(
                    request, 'Ha ocurrido un error al crear la ruta')
                messages.error(
                    request, 'la ciudad de origen no puede ser el mismo que el detino')
                return redirect('ruta_create')
            form.save()
            messages.success(request, 'La ruta fue creada exitosamente')
            return redirect('ruta_list')
        else:
            messages.error(request, 'Ha ocurrido un error al crear la ruta')
    else:
        form = RutaForm()
    return render(request, 'rutas/ruta_create.html', {'form': form})


def rutaBorrar(request, pk):
    try:
        ruta = Ruta.objects.get(pk=pk)
    except Ruta.DoesNotExist:
        messages.error(request, 'La ruta no existe')
        return redirect('ruta_list')

    if request.method == 'POST':
        ruta.delete()
        messages.success(request, 'La ruta fue eliminada exitosamente')
        return redirect('ruta_list')
    return render(request, 'rutas/ruta_delete.html', {'ruta': ruta})


def rutaEdit(request, pk):
    try:
        ruta = Ruta.objects.get(pk=pk)
    except Ruta.DoesNotExist:
        messages.error(request, 'La ruta no existe')
        return redirect('ruta_list')

    if request.method == 'POST':
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            form.save()
            messages.success(request, 'La ruta fue actualizada exitosamente')
            return redirect('ruta_list')
        else:
            messages.error(
                request, 'Ha ocurrido un error al actualizar la ruta')
    else:
        form = RutaForm(instance=ruta)
    return render(request, 'rutas/ruta_update.html', {'form': form, 'ruta_id': pk})


def login(request):
    return render(request, 'blog/login.html')


def crear_asientos(bus, cantidad_asientos):
    for i in range(cantidad_asientos):
        Asientos.objects.create(numero=i+1, bus=bus)


def busCreate(request):
    posts = Bus.objects.all()

    if request.method == 'POST':
        bus_form = BusForm(request.POST)

        if bus_form.is_valid():
            bus = bus_form.save()  # Guardar el objeto Bus

            # Obtener la cantidad de asientos del formulario
            cantidad_asientos = bus_form.cleaned_data['cantidadAsientos']

            # Crear los asientos asociados al objeto Bus
            crear_asientos(bus, cantidad_asientos)

            messages.success(
                request, 'El bus y los asientos fueron creados exitosamente')
            return redirect('bus_list')
        else:
            messages.error(
                request, 'Ha ocurrido un error al crear el bus y los asientos')
    else:
        bus_form = BusForm()

    return render(request, 'buses/bus_create.html', {'bus_form': bus_form, 'bus': posts})


def bus_list(request):
    buses = Bus.objects.all()
    form = BusForm()

    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            # Agregar mensajes de éxito o redireccionamiento si es necesario

    context = {
        'buses': buses,
        'form': form
    }

    return render(request, 'buses/bus_list.html', context)


def ciudadCreate(request):
    posts = Ciudades.objects.all()

    if request.method == 'POST':
        post_form = CiudadForm(request.POST)

        if post_form.is_valid():
            temp = post_form.save(commit=False)
            temp.author = request.user
            temp.save()
            messages.success(
                request, 'La publicación fue guardada exitosamente')
        else:
            messages.error(
                request, 'Ha ocurrido un error al guardar la publicación')

    else:
        post_form = CiudadForm()

    Ciudades_form = CiudadForm()

    return render(request, 'ciudades/ciudad_create.html', {'ciudades': posts, 'formulario': Ciudades_form})


def ciudad_list(request):
    ciudades = Ciudades.objects.all()
    form = CiudadForm()

    if request.method == 'POST':
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            # Agregar mensajes de éxito o redireccionamiento si es necesario

    context = {
        'ciudades': ciudades,
        'form': form
    }

    return render(request, 'ciudades/ciudad_list.html', context)


def horariosBusesLista(request):
    Hora_b = Horarios_buses.objects.all()
    return render(request, 'Horarios_buses/Horarios_buses_list.html', {'Hora_b': Hora_b})


def horiariosBusesCreacion(request):
    if request.method == 'POST':
        form = Horarios_busesForm(request.POST)
        if form.is_valid():
            horario_buses = form.save(commit=False)

            Hoy = date.today()

            if Hoy >= horario_buses.fecha or Hoy == horario_buses.fecha:
                messages.error(
                    request, 'Ha ocurrido un error al crear el horario de los buses.')
                messages.error(
                    request, 'No se puede crear un horario para el pasado o el presente.')
                return redirect('Horarios_buses_create')
            else:
                horario_buses.save()

                bus = horario_buses.bus
                asientos = Asientos.objects.filter(bus=bus)

                disponibilidades = []
                for asiento in asientos:
                    disponibilidad = Disponibilidad(
                        bus=bus,
                        asiento=asiento,
                        ruta=horario_buses.ruta,
                        horario=horario_buses.horario,
                        fecha=horario_buses.fecha,
                        disponible=True
                    )
                    disponibilidades.append(disponibilidad)

                Disponibilidad.objects.bulk_create(disponibilidades)

                messages.success(
                    request, 'El horario del bus fue creado exitosamente')
                return redirect('Horarios_buses_list')
        else:
            messages.error(
                request, 'Ha ocurrido un error al crear el horario de los buses')
    else:
        form = Horarios_busesForm()
    return render(request, 'Horarios_buses/Horarios_buses_create.html', {'form': form})


def horariosBusesBorrar(request, pk):
    try:
        Hora_b = Horarios_buses.objects.get(pk=pk)
    except Horarios_buses.DoesNotExist:
        messages.error(request, 'El horario del bus no existe')
        return redirect('Horarios_buses_list')

    if request.method == 'POST':
        disponibilidades = Disponibilidad.objects.filter(
            fecha=Hora_b.fecha, horario=Hora_b.horario, bus=Hora_b.bus)

        for disponibilidad in disponibilidades:
            if not disponibilidad.disponible:
                messages.error(
                    request, 'No se puede eliminar el horario del bus debido a que ya hay una compra.')
                return redirect('Horarios_buses_list')

        disponibilidades.delete()

        Hora_b.delete()
        messages.success(
            request, 'El horario del bus fue eliminado exitosamente')
        return redirect('Horarios_buses_list')

    return render(request, 'Horarios_buses/Horarios_buses_delete.html', {'Hora_b': Hora_b})


def horariosBusesEdit(request, pk):
    try:
        Hora_b = Horarios_buses.objects.get(pk=pk)
        Hora_a = Horarios_buses.objects.get(pk=pk)
    except Horarios_buses.DoesNotExist:
        messages.error(request, 'El horario del bus no existe')
        return redirect('Horarios_buses_list')

    if request.method == 'POST':
        form = Horarios_busesForm(request.POST, instance=Hora_b)
        if form.is_valid():

            disponibilidades = Disponibilidad.objects.filter(
                fecha=Hora_a.fecha,
                horario=Hora_a.horario,
                bus=Hora_a.bus
            )

            for disponibilidad in disponibilidades:
                if disponibilidad.disponible:
                    disponibilidad.fecha = Hora_b.fecha
                    disponibilidad.horario = Hora_b.horario
                    disponibilidad.bus = Hora_b.bus
                    disponibilidad.ruta = Hora_b.ruta
                    disponibilidad.save()
                else:
                    messages.error(
                        request, 'No se puede editar un horario con boletos vendidos.')
                    return redirect('Horarios_buses_update')

            form.save()
            messages.success(
                request, 'El horario del bus fue actualizado exitosamente')
            return redirect('Horarios_buses_list')
        else:
            messages.error(
                request, 'Ha ocurrido un error al actualizar el horario del bus')
    else:
        form = Horarios_busesForm(instance=Hora_b)

    return render(request, 'Horarios_buses/Horarios_buses_update.html', {'form': form, 'Hora_b_id': pk})


def disponibilidadLista(request):
    disponibilidades = Disponibilidad.objects.all()
    return render(request, 'disponibilidades/disponibilidad_list.html', {'disponibilidades': disponibilidades})


def clienteLista(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})


def clienteCreacion(request):
    if request.method == 'POST':
        Tclientes = Cliente.objects.all()
        cliente_form = ClienteForm(request.POST)
        cliente = cliente_form.save(commit=False)

        if cliente_form.is_valid():
            Rut = str(cliente.rut)
            for clientes in Tclientes:
                if cliente.rut == clientes.rut:
                    return redirect('reserva_create', clientes.id)
            if validar_rut(Rut):
                cliente_form.save()
                messages.success(
                    request, 'Datos fueron ingresados exitosamente')
                if request.user.is_authenticated:
                    return redirect('cliente_list')
                else:
                    return redirect('reserva_create', cliente.id)

            else:
                messages.error(
                    request, 'Ha ocurrido un error, el rut no es válido')
                if request.user.is_authenticated:
                    return redirect('cliente_create')
                else:
                    return redirect('cliente_create')
        else:
            messages.error(
                request, 'Ha ocurrido un error al guardar los datos.')
    else:
        cliente_form = ClienteForm()
    return render(request, 'clientes/cliente_create.html', {'cliente_form': cliente_form})


def clienteBorrar(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        messages.error(request, 'El cliente no existe')
        return redirect('cliente_list')

    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'El cliente fue eliminado exitosamente')
        return redirect('cliente_list')
    return render(request, 'clientes/cliente_delete.html', {'cliente': cliente})


def clienteEdit(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        messages.error(request, 'El cliente no existe')
        return redirect('cliente_list')

    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, instance=cliente)
        if cliente_form.is_valid():
            cliente_form.save()
            messages.success(
                request, 'El cliente fue actualizado exitosamente')
            return redirect('cliente_list')
        else:
            messages.error(
                request, 'Ha ocurrido un error al actualizar al cliente')
    else:
        cliente_form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_update.html', {'cliente_form': cliente_form, 'cliente_id': pk})


def crear_reserva(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        messages.error(request, 'El cliente no existe')
        return redirect('reserva_create', cliente.id)

    disponibilidades = Disponibilidad.objects.all()
    reservas = []

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            disponibilidad_ids = request.POST.getlist('disponibilidad_id')

            ruta_id = request.POST.get('ruta')

            reserva = form.save(commit=False)
            disponibilidades = Disponibilidad.objects.filter(
                fecha=reserva.fechaReserva, horario=reserva.horarioReserva, ruta=ruta_id)
            for disponibilidad_id in disponibilidad_ids:
                reserva = form.save(commit=False)
                reserva.cliente = cliente
                disponibilidad = Disponibilidad.objects.get(
                    id=disponibilidad_id)
                print(disponibilidad.disponible)
                if disponibilidad.disponible:
                    reserva.ruta = disponibilidad.ruta
                    reserva.asiento = disponibilidad.asiento
                    reserva.fechaReserva = disponibilidad.fecha
                    reserva.horarioReserva = disponibilidad.horario
                    reserva.bus = disponibilidad.bus
                    reserva.save()
                    print(disponibilidad_id)
                    disponibilidad.disponible = False
                    disponibilidad.save()
                    print(disponibilidad.disponible)
                    reservas.append(reserva)
                else:
                    messages.error(
                        request, 'No se puede revender un horario con boletos vendidos.')

    else:
        form = ReservaForm()

    return render(request, 'reservas/reserva_create.html', {'form': form, 'disponibilidades': disponibilidades, 'reservas': reservas})


class BusUpdateView(UpdateView):
    model = Bus
    form_class = BusForm
    template_name = 'buses/bus_update.html'
    success_url = '/buses/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bus_id'] = self.object.id
        return context


class BusDeleteView(DeleteView):
    model = Bus
    template_name = 'buses/bus_delete.html'
    success_url = '/buses/'


# Esto para los destinos


class CiudadUpdateView(UpdateView):
    model = Ciudades
    form_class = CiudadForm
    template_name = 'ciudades/ciudad_update.html'
    success_url = '/ciudades/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ciudad_id'] = self.object.id
        return context


class CiudadDeleteView(DeleteView):
    model = Ciudades
    template_name = 'ciudades/ciudad_delete.html'
    success_url = '/ciudades/'

# Esto para los origenes


def validar_rut(rut):
    rut = rut.replace(".", "")  # Eliminar puntos del Rut
    rut = rut.replace("-", "")  # Eliminar guion del Rut

    if len(rut) < 2:
        return False

    num_base = rut[:-1]
    dig_verif = rut[-1].upper()

    calculo_digito = []  # Lista que tendrá los valores que cambiarán para el cálculo
    # Lista que posee las cantidades a utilizar para el cálculo
    multiplicador = [2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6, 7]

    # Ciclo para verificar caracteres no válidos
    for i in range(len(num_base)):
        # En caso de que tenga puntos o comas retorna False
        if num_base[i] == "." or num_base[i] == ",":
            return False
        if num_base[i] == "-":  # En caso de que tenga guión retorna False
            return False

    primera_suma = 0
    segunda_suma = 0

    # Cálculo del dígito verificador
    for i in range(len(num_base)):
        calculo_digito.append(
            int(num_base[len(num_base) - 1 - i]) * multiplicador[i])
        primera_suma += calculo_digito[i]

    segunda_suma = primera_suma // 11
    segunda_suma = segunda_suma * 11
    primera_suma = primera_suma - segunda_suma
    digito_esperado = 11 - primera_suma

    if digito_esperado == 11:
        digito_esperado = "0"
    elif digito_esperado == 10:
        digito_esperado = "K"
    else:
        digito_esperado = str(digito_esperado)

    return digito_esperado == dig_verif
