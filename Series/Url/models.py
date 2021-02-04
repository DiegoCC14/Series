from django.db import models

# Create your models here.

class Series_Peliculas(models.Model): #Series y peliculas en general
	nombre = models.CharField(max_length=50 , primary_key = True , blank=False ,null=False) #nombre de la pelicula
	tipo = models.CharField(max_length=50 , blank=False ,null=False) #Pelicula o Serie
	descripcion_corta = models.CharField(max_length=150 , blank=False ,null=False) #descripcion de la pelicula
	year = models.IntegerField(default=0) #anio de la pelicula o serie
	image = models.ImageField() #Imagen de la pelicula 


class Temporada_de_Serie(models.Model): #Contiene link de temporadas
	nombre = models.CharField(max_length=50 , primary_key = True , blank=False ,null=False) #nombre de la pelicula
	descripcion_corta = models.CharField(max_length=150 , blank=False ,null=False)
	nombre_temporada = models.CharField(max_length=50 , blank=False ,null=False) #nombre de la pelicula
	temporada_nro = models.IntegerField(default=0) #anio de la pelicula
	year = models.IntegerField(default=1900) #anio de la pelicula
	cant_capitulos = models.IntegerField(default=1) #Cantidad de capitulos
	image = models.ImageField() #Imagen de la pelicula o serie

class Capitulo_Serie(models.Model): #Individual
	nombre = models.CharField(max_length=50 , blank=False ,null=False) #Nombre de la serie
	nombre_capitulo = models.CharField(max_length=50 , blank=False ,null=False)
	temporada = models.IntegerField(default=0) 
	capitulo = models.IntegerField(default=0)
	descripcion = models.CharField(max_length=250 , blank=False ,null=False)
	url = models.URLField() #URL del capitulo

class Pelicula(models.Model): #Individual
	nombre = models.CharField(max_length=50 , blank=False ,null=False) 
	descripcion = models.CharField(max_length=250 , blank=False ,null=False)
	url = models.URLField() #URL de la pelicula

	