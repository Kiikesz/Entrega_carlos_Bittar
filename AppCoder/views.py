from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor

# Create your views here.


def inicio(request):

    return HttpResponse("hola como estas?")

def agregar_profesor(request):
    
    profe1 = Profesor(nombre="pepe", apellido="Quintero", email="pepe@xs.com", profesion= "Desarrollador")
    profe1.save()
    HttpResponse("hemos agregado un profesor a la BD.")