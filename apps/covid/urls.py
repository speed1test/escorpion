from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('pruebas_resumen', views.pruebas_resumen , name ="pruebas_resumen"),
	path('pruebas_resumen_genero', views.pruebas_resumen_genero , name ="pruebas_resumen_genero"),


]
