from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        

def saludo(request):
    p1=Persona("Ruben","Lozano")
    # nombre="juan"
    # apellido="lopez"

    temasdelcurso=["plantillas","modelos","formularios","vistas","despliegue"]
    ahora=datetime.datetime.now()
    # doc_externo = open("C:/xampp/htdocs/django/Django/prueba/plantillas/miplantilla.html")
    # plt = Template(doc_externo.read())
    # doc_externo.close()
    #doc_externo=get_template('miplantilla.html')

    # ctx = Context({"nombre_persona": p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temasdelcurso})
    #documento = doc_externo.render({"nombre_persona": p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temasdelcurso})
    return render(request,"miplantilla.html",{"nombre_persona": p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora, "temas":temasdelcurso})
def cursoC(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"cursoC.html",{"dameFecha":fecha_actual})
def cursoCss(request):
    fecha_actual = datetime.datetime.now()
    return render(request,"cursoCss.html",{"dameFecha":fecha_actual})

def despedida(request):

    return HttpResponse("Hasta luego")

def fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = f"<html><body><h1>Fecha y hora actuales {fecha_actual}</h1></body></html>"
    return HttpResponse(documento)

def calculoedad(request, agno):
    edadActual = 18
    periodo = agno - 2023
    edadFutura = edadActual + periodo
    documento = f"<html><body><h2>En el año {agno} tendrás {edadFutura} años</h2></body></html>"
    return HttpResponse(documento)

def registro(request):
    return render(request,"registro.html", {})



