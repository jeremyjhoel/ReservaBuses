"""Reserva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Reservar.views import index
from Reservar.views import busCreate, bus_list, BusUpdateView, BusDeleteView
from Reservar.views import ciudad_list, ciudadCreate, CiudadDeleteView, CiudadUpdateView
from Reservar.views import rutaLista, rutaCreacion, rutaBorrar, rutaEdit
from Reservar.views import horariosBusesLista, horiariosBusesCreacion, horariosBusesEdit, horariosBusesBorrar
from Reservar.views import clienteLista, clienteCreacion, clienteBorrar, clienteEdit
from Reservar.views import horario_list, horarioCreate, HorarioDeleteView, HorarioUpdateView
from Reservar.views import fecha_list, fechaCreate, FechaDeleteView, FechaUpdateView
from Reservar.views import crear_reserva
from Reservar.views import disponibilidadLista

app_name = 'Reservar'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', index, name='index'),
    path('accounts/', include('django.contrib.auth.urls'), name='logout'),
    path('reservas/create/<int:pk>', crear_reserva, name='reserva_create'),

    path('disponibilidades/', disponibilidadLista, name='disponibilidad_list'),

    path('buses/', bus_list, name='bus_list'),
    path('buses/create/', busCreate, name='bus_create'),
    path('buses/update/<int:pk>/', BusUpdateView.as_view(), name='bus_update'),
    path('buses/delete/<int:pk>/', BusDeleteView.as_view(), name='bus_delete'),

    path('fechas/', fecha_list, name='fecha_list'),
    path('fechas/create/', fechaCreate, name='fecha_create'),
    path('fechas/update/<int:pk>/', FechaUpdateView.as_view(), name='fecha_update'),
    path('fechas/delete/<int:pk>/', FechaDeleteView.as_view(), name='fecha_delete'),

    path('horarios/', horario_list, name='horario_list'),
    path('horarios/create/', horarioCreate, name='horario_create'),
    path('horarios/update/<int:pk>/',
         HorarioUpdateView.as_view(), name='horario_update'),
    path('horarios/delete/<int:pk>/',
         HorarioDeleteView.as_view(), name='horario_delete'),

    path('ciudades/', ciudad_list, name='ciudad_list'),
    path('ciudades/create/', ciudadCreate, name='ciudad_create'),
    path('ciudades/update/<int:pk>/',
         CiudadUpdateView.as_view(), name='ciudad_update'),
    path('ciudades/delete/<int:pk>/',
         CiudadDeleteView.as_view(), name='ciudad_delete'),

    path('rutas/', rutaLista, name='ruta_list'),
    path('rutas/create/', rutaCreacion, name='ruta_create'),
    path('rutas/update/<int:pk>/', rutaEdit, name='ruta_update'),
    path('rutas/delete/<int:pk>/', rutaBorrar, name='ruta_delete'),

    path('Horarios_buses/', horariosBusesLista,
         name='Horarios_buses_list'),
    path('Horarios_buses/create/', horiariosBusesCreacion,
         name='Horarios_buses_create'),
    path('Horarios_buses/update/<int:pk>/',
         horariosBusesEdit, name='Horarios_buses_update'),
    path('Horarios_buses/delete/<int:pk>/',
         horariosBusesBorrar, name='Horarios_buses_delete'),

    path('clientes/', clienteLista, name='cliente_list'),
    path('clientes/create/', clienteCreacion, name='cliente_create'),
    path('clientes/delete/<int:pk>/', clienteBorrar, name='cliente_delete'),

]
