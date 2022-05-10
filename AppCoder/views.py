from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso, Profesor
from AppCoder.forms import CursoFormulario, ProfesorFormulario

# Create your views here.
def curso(request):
    if request.method == 'POST': #al hacer click al enviar
        miFormulario = CursoFormulario(request.POST) #aquí me llega toda la info del formulario
        print(miFormulario)
    
        if miFormulario.is_valid():                     #comprobar si la info es válida / si pasó la validación de Django
            
            informacion = miFormulario.cleaned_data     #diccionario con la info del formulario
            
            #creando un curso (modelo) usando la info recibida
            curso = Curso(nombre = informacion["curso"], camada = informacion["camada"]) 
            curso.save()

            #una vez guardado mostramos la plantilla de inicio / volvemos a donde queremos
            return render(request, 'AppCoder/inicio.html')                                
    
    else:
        # si el método no es post, quiero que me muestre el formulario vacío
        miFormulario = CursoFormulario() #Formulario vacío para construir el html
    
    return render(request, 'AppCoder/curso.html', {"miFormulario": miFormulario})
    
def estudiante(request):
    return render(request, 'AppCoder/estudiante.html')

def entregable(request):
    return render(request, 'AppCoder/entregable.html')
    
def profesor(request):
    if request.method == "POST": #al hacer click al enviar
        
        miFormulario = ProfesorFormulario(request.POST) #aquí me llega toda la info del formulario
        print(miFormulario)
    
        if miFormulario.is_valid(): # comprobar si la info es válida / si pasó la validación de Django
            info = miFormulario.cleaned_data #diccionario con la info del formulario
            
            #creando un curso (modelo) usando la info recibida
            profe = Profesor(nombre = info["nombre"], apellido = info["apellido"], email = info["email"], profesion = info["profesion"]) 
            profe.save()
            
            #una vez guardado mostramos la plantilla de inicio / volvemos a donde queremos
            return render(request, 'AppCoder/inicio.html') 
    
    else:
        # si el método no es post, quiero que me muestre el formulario vacío
        miFormulario = ProfesorFormulario() #Formulario vacío para construir el html
        
    return render(request, 'AppCoder/profesor.html', {"miFormulario": miFormulario})

def certificacion(request):
    return render(request, 'AppCoder/certificacion.html')

def cursoFormulario(request):
    return

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']} "
    
    if request.GET["camada"]:
        #respuesta = f"Estoy buscando la camada nro: {request.GET['camada']} "
        camada = request.GET["camada"]
        #cursos = Curso.objects.filter(camada__icontains=camada) #icontains significa que las camadas tienen el numero de camada que estamos buscando
        cursos = Curso.objects.filter(camada__iexact=camada)
        
        return render(request, 'AppCoder/resultadosBusqueda.html', {"cursos": cursos, "camada": camada})
    else:
        respuesta = "No eviaste datos"
        
    return HttpResponse(respuesta)

def profesorFormulario(request):
    if request.method == "POST": #al hacer click al enviar
        
        miFormulario = ProfesorFormulario(request.POST) #aquí me llega toda la info del formulario
        print(miFormulario)
    
        if miFormulario.is_valid(): # comprobar si la info es válida / si pasó la validación de Django
            info = miFormulario.cleaned_data #diccionario con la info del formulario
            
            #creando un curso (modelo) usando la info recibida
            profe = Profesor(nombre = info["nombre"], apellido = info["apellido"], email = info["email"], profesion = info["profesion"]) 
            profe.save()
            
            #una vez guardado mostramos la plantilla de inicio / volvemos a donde queremos
            return render(request, 'AppCoder/inicio.html') 
    
    else:
        # si el método no es post, quiero que me muestre el formulario vacío
        miFormulario = ProfesorFormulario() #Formulario vacío para construir el html
        
    return render(request, 'AppCoder/profesorFormulario.html', {"miFormulario": miFormulario})