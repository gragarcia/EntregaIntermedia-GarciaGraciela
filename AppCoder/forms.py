from django import forms


class CursoFormulario(forms.Form):
    #Especificar los campos
    
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class ProfesorFormulario(forms.Form):
    #Especificar los campos
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()