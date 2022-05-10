# ProyectoCoder
Este proyecto se basa en el desarrollo de una página web relacionada a la gestión de una plataforma de una institución educativa.
El proyecto es AppCoder y aquí se listan las operaciones que se pueden realizar desde la página hasta el momento: 

1- Para entrar a la página principal ingresar al siguiente link: localhost/AppCoder
2- También existen otros links (donde se implementa la herencia de html)
	Los diversos tabs existentes en la página de inicio hacen referencia a: 

	- Profesores: (http://127.0.0.1:8000/AppCoder/profesores/)
	- Cursos: (http://127.0.0.1:8000/AppCoder/curso/)
	- Estudiantes: (http://127.0.0.1:8000/AppCoder/estudiante/)
	- Entregables: (http://127.0.0.1:8000/AppCoder/entregable/)
	- Certificaciones: (http://127.0.0.1:8000/AppCoder/certificaciones/)


3- Para poder crear nuevos cursos, se lo puede hacer desde la página de Cursos link (http://127.0.0.1:8000/AppCoder/curso/) o seleccionando el tab Cursos en la página de Inicio

Se debe ingresar el nombre del curso en el campo "nombre" y luego ingresar el nro de la camada en el campo llamado "camada"

Al finalizar hacer click en el botón Enviar.

*Para poder verificar que el curso se ha creado correctamente ingresar al siguiente link: http://127.0.0.1:8000/admin/
Loguearse con el usuario temporal generado: tutorJ  password: tutorDjango1

4- Una vez creado un nuevo curso se puede obtener la información de los cursos que pertencen a una camada en particular entrando al siguietne link: http://127.0.0.1:8000/AppCoder/busquedaCamada/
Al hacer click en el botón Buscar, este nos lleva a otro formulario que muestra el resultado