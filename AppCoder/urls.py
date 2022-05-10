from django.urls import path
from AppCoder import views

urlpatterns = [
    path('curso/', views.curso, name='Cursos'),
    path('estudiante/', views.estudiante, name='Estudiantes'),
    path('entregable/', views.entregable, name ='Entregables'),
    path('profesores/', views.profesor, name ='Profesores'),
    path('certificaciones/', views.certificacion, name ='Certificaciones'),
    #path('cursoFormulario/', views.cursoFormulario, name ='CursoFormulario'),
    path('profesorFormulario/', views.profesorFormulario, name ='ProfesorFormulario'),
    path('', views.inicio, name='Inicio'),
    path('busquedaCamada/', views.busquedaCamada, name ='BusquedaCamada'),
    path('buscar/', views.buscar),
    #path('listaProfes/', views.leerProfesores.html, name= "ListaProfesores"),
]