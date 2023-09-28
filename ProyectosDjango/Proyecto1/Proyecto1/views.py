from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):
    def __init__(self, nombre, cognom):
        self.nombre=nombre

        self.cognom=cognom



class habitant(object):
     def __init__(self, nombre, cognom, any, ciutat):
         self.nombre=nombre
         self.cognom=cognom
         self.any=any
         self.ciutat=ciutat





        
        

def saludo(request):
    h1=habitant("David","Blanco","2004","Badalona")
    

    p1=Persona("David","Blanco")
    #nombre="David"
    #cognom="Blanco"
    temas=[]
    ahora=datetime.datetime.now()

    doc_externo=open("C:/Users/Administrator/Desktop/ProyectosDjango/Proyecto1/Proyecto1/plantillas/plantilla2.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_habitant":h1.nombre, "cognom_habitant":h1.cognom, "any_habitant":h1.any,"ciutat_habitant":h1.ciutat ,"fecha_actual":ahora, 
                 "moduls":["m6","m8","m7","m9","m12"]})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Adios") 

def damefecha(request):
    fecha_actual=datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
    Fecha y Horas actuales %s
    </h1>
    </body>
    </html>"""% fecha_actual   

    return HttpResponse(documento)
def calcularEdad(request, agno):

    edadActual=19
    periodo=agno-2023
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(agno, edadFutura)

    return HttpResponse(documento)

# Ejercicio 2
def ruta1(request):
    return HttpResponse("Esta es la ruta 1") 

def ruta2(request):
    return HttpResponse("Esta es la ruta 2") 

def ruta3(request):
    return HttpResponse("Esta es la ruta 3") 

def diaActual(request):
    dia_actual=datetime.date.today()
    documento = """<html>
    <body>
    <h1>
     Hoy es %s
    </h1>
    </body>
    </html>"""% dia_actual 
    return HttpResponse(documento)

def diaActual(request):
    dia_actual=datetime.date.today()
    dia_final=datetime.date(2024,1,1)
    resultado=dia_final-dia_actual
    documento = """
    <html>
        <body>
            <table>
                <tr>
                    <td style="border:1px solid">Hoy es</td>
                    <td style="border:1px solid">Lo que falta para año nuevo</td>
                </tr>
                <tr>
                    <td style="border:1px solid">%s</td>
                    <td style="border:1px solid">%s</td>
                </tr>
            </table>
        </body>
    </html>"""% (dia_actual,resultado)
    return HttpResponse(documento)

def datosUsuario(request, nombre, agno):
    if agno>2050:
        documento= "Error"
    else:
        edad=2023-agno
        documento= "Tu nombre es: %s y tu edad es %s" %(nombre,edad)
        if agno<1900:
            documento= "Error"
    return HttpResponse(documento)

        
    
    
    