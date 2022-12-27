from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def listar_cursos(request):
    diccionario = {'Titulo': 'Listado de Cursos'}

    return render(request, "cursos.html", diccionario)

def listar_carreras(request):
    diccionario = {'Titulo': 'Listado de Carreras'}

    return render(request, "carreras.html", diccionario)

def crear_curso(request):
    diccionario = {'Titulo': 'Agregar Curso'}

    return render(request, "crear_curso.html", diccionario)

def crear_carrera(request):
    diccionario = {'Titulo': 'Agregar Carrera'}

    return render(request, "crear_carrera.html", diccionario)