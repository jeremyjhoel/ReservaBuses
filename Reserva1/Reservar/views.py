from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Cliente, Bus, Ruta, Ciudades, Asientos, Horarios_buses, Disponibilidad, Reserva, Fecha, Horario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BusForm, RutaForm, CiudadForm, Horarios_busesForm, ClienteForm, ReservaForm, FechaForm, HorarioForm
from django.urls import reverse_lazy
from datetime import date


def index(request):
    ruta = Ruta.objects.all()
    horarios = Horarios_buses.objects.all()
    return render(request, 'index.html', {'ruta': ruta, 'horarios': horarios})


def rutaLista(request):
    rutas = Ruta.objects.all()
    return render(request, 'rutas/ruta_list.html', {'rutas': rutas})


def rutaCreacion(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        rutas = form.save(commit=False)
        if form.is_valid():
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
            auxiliar = False
            auxiliar1 = True
            rutas = Ruta.objects.all()

            if Hoy >= horario_buses.fecha.fecha or Hoy == horario_buses.fecha.fecha:
                messages.error(
                    request, 'Ha ocurrido un error al crear el horario de los buses.')
                messages.error(
                    request, 'No se puede crear un horario para el pasado o el presente.')
                return redirect('Horarios_buses_create')

            else:
                Hora_bs = Horarios_buses.objects.all()
                for hora_b in Hora_bs:
                    if (hora_b.horario.horario == horario_buses.horario.horario and hora_b.fecha.fecha == horario_buses.fecha.fecha) and auxiliar:
                        messages.error(
                            request, 'Ha ocurrido un error al crear el horario de los buses.')
                        messages.error(
                            request, 'No se puede crear un horario para la misma ruta al mismo tiempo')
                        auxiliar1 = False
                        break
                for ruta in rutas:
                    if (str(ruta.ciudadO.ciudad) == str(horario_buses.ciudadO) and str(ruta.ciudadD.ciudad) == str(horario_buses.ciudadD) and auxiliar1):
                        horario_buses.save()
                        bus = horario_buses.bus
                        disponibilidades = []
                        asientos = Asientos.objects.filter(bus=bus)
                        for asiento in asientos:
                            disponibilidad = Disponibilidad(
                                bus=bus,
                                asiento=asiento,
                                ciudadO=horario_buses.ciudadO,
                                ciudadD=horario_buses.ciudadD,
                                horario=horario_buses.horario,
                                fecha=horario_buses.fecha,
                                disponible=True
                            )
                            disponibilidades.append(disponibilidad)

                        Disponibilidad.objects.bulk_create(disponibilidades)
                        messages.success(
                            request, 'El horario del bus fue creado exitosamente')
                        auxiliar = False
                        break
                    elif auxiliar and not auxiliar1:
                        auxiliar = True
                if auxiliar:
                    messages.error(
                        request, 'Ha ocurrido un error al crear el horario de los buses')
                    messages.error(
                        request, 'No hay ruta disponible')
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
    dato = request.POST.get('dato')
    if dato != None:
        for disponibilidad in disponibilidades:
            if int(disponibilidad.id) == int(dato):
                disponibilidad.disponible = True
                disponibilidad.save()
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
            correo = cliente.email
            if '@' in correo:
                auxiliar = correo[correo.find('@'):]
                if ('.' in auxiliar):
                    auxiliar1 = auxiliar[auxiliar.find('.'):]
                    if not (len(auxiliar1) != 0):
                        messages.error(
                            request, 'Ha ocurrido un error no se ha ingresado un correo electrónico válido')
                        return redirect('cliente_create')
                else:
                    messages.error(
                        request, 'Ha ocurrido un error no se ha ingresado un correo electrónico válido')
                    return redirect('cliente_create')
            else:
                messages.error(
                    request, 'Ha ocurrido un error no se ha ingresado un correo electrónico válido')
                return redirect('cliente_create')

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
            auxiliar = None
            auxiliar1 = None
            auxiliar2 = None
            auxiliar3 = None
            disponibilidad_ids = request.POST.getlist('disponibilidad_id')

            rutas = Ruta.objects.all()
            reserva = form.save(commit=False)
            horarios = Horario.objects.all()
            fechas = Fecha.objects.all()

            for horario in horarios:
                if str(horario.horario) == str(reserva.horario.horario):
                    auxiliar = horario.id

            for fecha in fechas:
                if str(fecha.fecha) == str(reserva.fecha.fecha):
                    auxiliar1 = fecha.id
                    print(auxiliar1)
            for ruta in rutas:
                if (str(ruta.ciudadO.ciudad) == str(reserva.ciudadO.ciudad)) and (str(ruta.ciudadD.ciudad) == str(reserva.ciudadD.ciudad)):
                    auxiliar2 = reserva.ciudadO
                    auxiliar3 = reserva.ciudadD
            disponibilidades = Disponibilidad.objects.filter(
                fecha=auxiliar1, horario=auxiliar, ciudadO=auxiliar2, ciudadD=auxiliar3)

            for disponibilidad_id in disponibilidad_ids:

                reserva = form.save(commit=False)
                reserva.cliente = cliente
                disponibilidad = Disponibilidad.objects.get(
                    id=disponibilidad_id)
                if disponibilidad.disponible:
                    reserva.ciudadO = disponibilidad.ciudadO
                    reserva.ciudadD = disponibilidad.ciudadD
                    reserva.asiento = disponibilidad.asiento
                    reserva.fechaReserva = disponibilidad.fecha
                    reserva.horarioReserva = disponibilidad.horario
                    reserva.bus = disponibilidad.bus
                    reserva.save()

                    disponibilidad.disponible = False
                    disponibilidad.save()
                    reservas.append(reserva)
            else:
                messages.error(
                    request, 'Ha ocurrido un eror')

        else:
            messages.error(
                request, 'No se puede revender un horario con boletos vendidos.')

    else:
        form = ReservaForm()

    return render(request, 'reservas/reserva_create.html', {'form': form, 'disponibilidades': disponibilidades, 'reservas': reservas})


def fechaCreate(request):
    posts = Fecha.objects.all()

    if request.method == 'POST':
        post_form = FechaForm(request.POST)

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
        post_form = FechaForm()

    fechas_form = FechaForm()

    return render(request, 'fechas/fecha_create.html', {'fechas': posts, 'fechas_form': fechas_form})


def fecha_list(request):
    fechas = Fecha.objects.all()
    form = FechaForm()

    if request.method == 'POST':
        form = FechaForm(request.POST)
        if form.is_valid():
            form.save()
            # Agregar mensajes de éxito o redireccionamiento si es necesario

    context = {
        'fechas': fechas,
        'form': form
    }

    return render(request, 'fechas/fecha_list.html', context)


class FechaUpdateView(UpdateView):
    model = Fecha
    form_class = FechaForm
    template_name = 'fechas/fecha_update.html'
    success_url = '/fechas/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha_id'] = self.object.id
        return context


class FechaDeleteView(DeleteView):
    model = Fecha
    template_name = 'fechas/fecha_delete.html'
    success_url = '/fechas/'


def horarioCreate(request):
    posts = Horario.objects.all()

    if request.method == 'POST':
        post_form = HorarioForm(request.POST)

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
        post_form = HorarioForm()

    horario_form = HorarioForm()

    return render(request, 'horarios/horario_create.html', {'horarios': posts, 'horario_form': horario_form})


def horario_list(request):
    horario = Horario.objects.all()
    form = HorarioForm()

    if request.method == 'POST':
        form = HorarioForm(request.POST)
        if form.is_valid():
            form.save()
            # Agregar mensajes de éxito o redireccionamiento si es necesario

    context = {
        'horario': horario,
        'form': form
    }

    return render(request, 'horarios/horario_list.html', context)


class HorarioUpdateView(UpdateView):
    model = Horario
    form_class = HorarioForm
    template_name = 'horarios/horario_update.html'
    success_url = '/horarios/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['horario_id'] = self.object.id
        return context


class HorarioDeleteView(DeleteView):
    model = Horario
    template_name = 'horarios/horario_delete.html'
    success_url = '/horarios/'


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
