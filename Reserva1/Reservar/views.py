from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Cliente, Bus, Ruta, Ciudades, Asientos, Disponibilidad
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BusForm, RutaForm, CiudadForm, AsientosForm, DisponibilidadForm
from django.urls import reverse_lazy


def index(request):

    return render(request, 'index.html')


def rutaLista(request):
    rutas = Ruta.objects.all()
    return render(request, 'rutas/ruta_list.html', {'rutas': rutas})


def rutaCreacion(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid():
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


def disponibilidadLista(request):
    disponibilidades = Disponibilidad.objects.all()
    return render(request, 'disponibilidades/disponibilidad_list.html', {'disponibilidades': disponibilidades})


def disponibilidadCreacion(request):

    if request.method == 'POST':
        form = DisponibilidadForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'La disponibilidad fue creada exitosamente')
            return redirect('disponibilidad_list')
        else:
            messages.error(
                request, 'Ha ocurrido un error al crear la disponibilidad')
    else:
        form = DisponibilidadForm()
    return render(request, 'disponibilidades/disponibilidad_create.html', {'form': form})


def disponibilidadBorrar(request, pk):
    try:
        disponibilidad = Disponibilidad.objects.get(pk=pk)
    except Disponibilidad.DoesNotExist:
        messages.error(request, 'La disponibilidad no existe')
        return redirect('disponibilidad_list')

    if request.method == 'POST':
        disponibilidad.delete()
        messages.success(
            request, 'La disponibilidad fue eliminada exitosamente')
        return redirect('disponibilidad_list')
    return render(request, 'disponibilidades/disponibilidad_delete.html', {'disponibilidad': disponibilidad})


def disponibilidadEdit(request, pk):
    try:
        disponibilidad = Disponibilidad.objects.get(pk=pk)
    except Disponibilidad.DoesNotExist:
        messages.error(request, 'La disponibilidad no existe')
        return redirect('disponibilidad_list')

    if request.method == 'POST':
        form = DisponibilidadForm(request.POST, instance=disponibilidad)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'La disponibilidad fue actualizada exitosamente')
            return redirect('disponibilidad_list')
        else:
            messages.error(
                request, 'Ha ocurrido un error al actualizar la disponibilidad')
    else:
        form = DisponibilidadForm(instance=disponibilidad)
    return render(request, 'disponibilidades/disponibilidad_update.html', {'form': form, 'disponibilidad_id': pk})


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
