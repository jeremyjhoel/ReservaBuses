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
from Reservar.views import RutaListView, RutaCreateView, RutaUpdateView, RutaDeleteView
from Reservar.views import destino_list, destinoCreate, DestinoDeleteView, DestinoUpdateView
from Reservar.views import origen_list, origenCreate, OrigenDeleteView, OrigenUpdateView, rutaLista, rutaCreacion, rutaBorrar, rutaEdit

app_name = 'Reservar'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', index, name='index'),
    path("accounts/", include("django.contrib.auth.urls"), name='logout'),

    path('buses/', bus_list, name='bus_list'),
    path('buses/create/', busCreate, name='bus_create'),
    path('buses/update/<int:pk>/', BusUpdateView.as_view(), name='bus_update'),
    path('buses/delete/<int:pk>/', BusDeleteView.as_view(), name='bus_delete'),

    path('destinos/', destino_list, name='destino_list'),
    path('destinos/create/', destinoCreate, name='destino_create'),
    path('destinos/update/<int:pk>/',
         DestinoUpdateView.as_view(), name='destino_update'),
    path('destinos/delete/<int:pk>/',
         DestinoDeleteView.as_view(), name='destino_delete'),

    path('origenes/', origen_list, name='origen_list'),
    path('origenes/create/', origenCreate, name='origen_create'),
    path('origenes/update/<int:pk>/',
         OrigenUpdateView.as_view(), name='origen_update'),
    path('origenes/delete/<int:pk>/',
         OrigenDeleteView.as_view(), name='origen_delete'),

    path('rutas/', rutaLista, name='ruta_list'),
    path('rutas/create/', rutaCreacion, name='ruta_create'),
    path('rutas/update/<int:pk>/', rutaEdit, name='ruta_update'),
    path('rutas/delete/<int:pk>/', rutaBorrar, name='ruta_delete'),
]
