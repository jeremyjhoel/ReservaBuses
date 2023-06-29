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
]
