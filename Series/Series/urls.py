"""Series URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from Series.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Inicio,name='Inicio'),
    path('Peliculas/',Peliculas,name='Peliculas'),
    path('Series/',Series,name='Series'),
    path('Serie_elegida/<str:nombre_serie>',Serie_Elegida,name='Serie_Elegida'),
    path('Eleccion_Capitulo/<str:serie_temporada>',Eleccion_Capitulo,name='Eleccion_Capitulo'),
    path('Pelicula_Elegida/<str:nombre_pelicula>' , Pelicula_Elejida , name='Pelicula_Elejida')
]
