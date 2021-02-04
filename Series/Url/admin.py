from django.contrib import admin
from .models import *
# Register your models here.

class Peliculas_Series_Generales(admin.ModelAdmin):
	search_fields = ['nombre','year']
	list_display = ('nombre','year')

class Serie_Individual(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ('nombre','capitulo')
class Pelicula_Individual(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ['nombre']

admin.site.register(Series_Peliculas,Peliculas_Series_Generales)
admin.site.register(Temporada_de_Serie,Peliculas_Series_Generales)
admin.site.register(Capitulo_Serie,Serie_Individual)
admin.site.register(Pelicula,Pelicula_Individual)

