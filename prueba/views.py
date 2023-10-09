from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):
    nombre="juan"
    apellido="lopez"
    ahora=datetime.datetime.now()
    doc_externo = open("C:/xampp/htdocs/Django/prueba/prueba/plantillas/miplantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona": nombre,"apellido_persona":apellido,"momento_actual":ahora})
    documento = plt.render(ctx)
    return HttpResponse(documento)

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


