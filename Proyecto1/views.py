from django.http import HttpResponse
from django.template import Template, Context




def saludo(request):
    return HttpResponse("hola mundo")



def landing(request):
    nom = "kike"
    ap = "bittar"
    diccionario = {"nombre":nom, "apellido":ap}
    mihtml = open(r"C:\Users\cbitt\OneDrive\Escritorio\Cursos\Coder\03-Python\VSC\django\Proyecto1\Proyecto1\plantilla_template\landing.html")
    plantilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context(diccionario)
    documento = plantilla.render(micontexto)
    return HttpResponse(documento)