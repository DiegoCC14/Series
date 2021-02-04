from django.shortcuts import redirect,render
from Url.models import *

def Inicio(request):
	Series = Series_Peliculas.objects.filter()
	diccionario = {'PyS':Series}
	return render(request,'Inicio.html',diccionario)

def Peliculas(request):
	Series = Series_Peliculas.objects.filter(tipo='Pelicula')
	diccionario = {'PyS':Series}
	return render(request,'Inicio.html',diccionario)

def Series(request):
	Series = Series_Peliculas.objects.filter(tipo='Serie')
	diccionario = {'PyS':Series}
	return render(request,'Inicio.html',diccionario)

def Serie_Elegida(request,nombre_serie):
	Serie = Series_Peliculas.objects.filter(nombre = nombre_serie)
	Temporadas = Temporada_de_Serie.objects.filter(nombre__icontains = nombre_serie) #icontains contiene valor dentro

	return render(request,'videos.html',{'Temporadas_serie':Temporadas,'serie':Serie[0]})

def Eleccion_Capitulo(request,serie_temporada):
	Capitulos = Capitulo_Serie.objects.filter(nombre=serie_temporada).order_by('capitulo')
	return render(request,'Capitulos_serie.html',{'Capitulos':Capitulos,'Nombre_Tem':serie_temporada})

def Pelicula_Elejida(request,nombre_pelicula):
	Peli = Pelicula.objects.filter(nombre=nombre_pelicula)
	return redirect(Peli[0].url) #Dirigimos hacia el link de la pelicula
