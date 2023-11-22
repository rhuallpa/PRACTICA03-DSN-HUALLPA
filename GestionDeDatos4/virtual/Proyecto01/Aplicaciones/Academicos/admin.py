from django.contrib import admin
from .models import Especialidad, Docente, Curso, Alumno, Contacto

admin.site.register(Especialidad)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Alumno)

admin.site.register(Contacto)