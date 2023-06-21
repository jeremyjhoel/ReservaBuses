from django.shortcuts import render
from .models import Cliente, Bus
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import BusForm
class BusListView(ListView):
    model = Bus
    template_name = 'buses/bus_list.html'
    context_object_name = 'buses'
    success_url = '/buses/'

class BusCreateView(CreateView):
    model = Bus
    form_class = BusForm
    template_name = 'buses/bus_create.html'
    success_url = '/buses/'

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
