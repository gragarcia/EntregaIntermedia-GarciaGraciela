from django.db import models

# Create your models here.
class Curso(models.Model):
      nombre = models.CharField(max_length=40)
      camada = models.IntegerField()
      
      def __str__(self):
          txt="{0} - {1}"
          return txt.format(self.camada, self.nombre)
          
      
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100) 
    email = models.EmailField()  
    
    def __str__(self):
          txt="{0} - {1}"
          return txt.format(self.apellido, self.nombre)  
    
    class Meta:
        verbose_name="Estudiantes"
        verbose_name_plural = "Estudiantes" 

class Profesor(models.Model):
    
    def __str__(self):
        return f"Nombre : {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    
    
    class Meta:
        verbose_name="Profesor"
        verbose_name_plural = "profesores"
    
class Entregable(models.Model):
    def __str__(self):
        return f"Nombre : {self.nombre} - Fecha de Entrega: {self.fechaDeEntrega} - Entregado: {self.entregado}"
    
    nombre = models.CharField(max_length=100) 
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()    
    
class Certificaciones(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha = models.DateField()
    
    class Meta:
        verbose_name="Certificaciones"
        verbose_name_plural = "Certificaciones"
        
