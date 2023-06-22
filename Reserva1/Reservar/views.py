from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Cliente, Bus, Ruta, Destino
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BusForm, RutaForm, DestinoForm


def index(request):

    return render(request, 'index.html')


def login(request):
    return render(request, 'blog/login.html')


def busCreate(request):
    posts = Bus.objects.all()

    if request.method == 'POST':
        post_form = BusForm(request.POST)

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
        post_form = BusForm()

    bus_form = BusForm()

    return render(request, 'buses/bus_create.html', {'bus': posts, 'formulario': bus_form})


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


def destinoCreate(request):
    posts = Destino.objects.all()

    if request.method == 'POST':
        post_form = DestinoForm(request.POST)

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
        post_form = DestinoForm()

    destino_form = DestinoForm()

    return render(request, 'destinos/destino_create.html', {'destinos': posts, 'formulario': destino_form})


def destino_list(request):
    destinos = Destino.objects.all()
    form = DestinoForm()

    if request.method == 'POST':
        form = DestinoForm(request.POST)
        if form.is_valid():
            form.save()
            # Agregar mensajes de éxito o redireccionamiento si es necesario

    context = {
        'destinos': destinos,
        'form': form
    }

    return render(request, 'destinos/destino_list.html', context)


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


# Esto para las rutas:

class RutaListView(ListView):
    model = Ruta
    template_name = 'rutas/ruta_list.html'
    context_object_name = 'rutas'
    success_url = '/rutas/'


class RutaCreateView(CreateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'rutas/ruta_create.html'
    success_url = '/rutas/'


class RutaUpdateView(UpdateView):
    model = Ruta
    form_class = RutaForm
    template_name = 'rutas/ruta_update.html'
    success_url = '/rutas/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ruta_id'] = self.object.id
        return context


class RutaDeleteView(DeleteView):
    model = Ruta
    template_name = 'rutas/ruta_delete.html'
    success_url = '/rutas/'

# Esto para los destinos


class DestinoUpdateView(UpdateView):
    model = Destino
    form_class = DestinoForm
    template_name = 'destinos/destino_update.html'
    success_url = '/destinos/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destino_id'] = self.object.id
        return context


class DestinoDeleteView(DeleteView):
    model = Destino
    template_name = 'destinos/destino_delete.html'
    success_url = '/destinos/'
