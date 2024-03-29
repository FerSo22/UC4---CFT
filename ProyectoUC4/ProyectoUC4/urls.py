"""ProyectoUC4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from ProyectoWeb.views import index, listar_carreras, listar_cursos, crear_carrera, crear_curso

urlpatterns = [
    path('', index, name="inicio"),
    path('inicio/', index, name="inicio"),
    path("cursos/", listar_cursos, name="listar_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("carreras/", listar_carreras, name="listar_carreras"),
    path("crear-carrera/", crear_carrera, name="crear_carrera"),
]
