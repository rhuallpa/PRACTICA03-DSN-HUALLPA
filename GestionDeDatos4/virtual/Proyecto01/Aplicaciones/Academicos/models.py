from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Docente(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    f_ingreso = models.DateField()
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.creditos} créditos)"


class Alumno(models.Model):
    id_alumno = models.CharField(primary_key=True, max_length=6)
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Contacto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    foto = models.ImageField(upload_to='fotos/')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
  

