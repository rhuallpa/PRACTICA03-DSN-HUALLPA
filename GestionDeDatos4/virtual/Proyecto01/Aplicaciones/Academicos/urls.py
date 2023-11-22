from django.urls import path
from . import views

urlpatterns = [
    path('curso', views.curso, name='curso'),
    path('docente', views.docente, name='docente'),
    path('especialidad', views.especialidad, name='especialidad'),
    path('alumno', views.alumno, name='alumno'),  # URL de la página de alumnos
    path('contacto', views.contacto, name='conta'),
 
    path('curso/registrar/', views.registrarcurso, name='registrar_curso'),
    path('registrardocente', views.registrardocente, name='registrardocente'),
    path('registrarespecialidad', views.registrarespecialidad, name='registrarespecialidad'),
    path('alumno/registrar/', views.registrar_alumno, name='registrar_alumno'),  # URL para registrar un nuevo alumno
    path('registrar_contacto/', views.registrar_contacto, name='registrar_contacto'),

    path('eliminarcurso/<str:codigo>/', views.eliminarcurso, name='eliminarcurso'),
    path('eliminardocente/<str:id>/', views.eliminardocente, name='eliminardocente'),
    path('eliminarespecialidad/<str:nombre>/', views.eliminarespecialidad, name='eliminarespecialidad'),
    path('eliminaralumno/<int:id_alumno>/', views.eliminar_alumno, name='eliminaralumno'),  # Corregido: eliminar_alumno en lugar de eliminaralumno
    path('eliminar_contacto/<str:codigo>/', views.eliminar_contacto, name='eliminar_contacto'),


    path('edicioncurso/<str:codigo>/', views.edicioncurso, name='edicioncurso'),
    path('ediciondocente/<str:id>/', views.ediciondocente, name='ediciondocente'),
    path('edicionespecialidad/<str:nombre>/', views.edicionespecialidad, name='edicionespecialidad'),
    path('edicionalumno/<int:id_alumno>/', views.edicionalumno, name='edicionalumno'),  # URL para la edición de un alumno
    path('edicion_contacto/<str:codigo>/', views.edicion_contacto, name='edicion_contacto'),




    path('editarcurso/<str:codigo>/', views.editarcurso, name='editar_curso'),
    path('editardocente/<int:id>/', views.editardocente, name='editar_docente'),
    path('editarespecialidad/<int:especialidad_id>/', views.editarespecialidad, name='editarespecialidad'),
    path('editaralumno/<int:id_alumno>/', views.editaralumno, name='editaralumno'),  # URL para editar un alumno   
    path('editar_contacto/<str:codigo>/', views.editar_contacto, name='editar_contacto'),



    path('buscar_curso', views.buscar_curso, name='buscar_curso'),
    path('buscar_docente', views.buscar_docente, name='buscar_docente'),
    path('buscar_especialidad', views.buscar_especialidad, name='buscar_especialidad'),
    path('buscar_alumno', views.buscar_alumno, name='buscar_alumno'),
    path('buscar_contacto', views.buscar_contacto, name='buscar_contacto'),


    path('', views.homes, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),  





]




