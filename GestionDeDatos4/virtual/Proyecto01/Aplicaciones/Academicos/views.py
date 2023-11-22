from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from datetime import datetime
from .models import Curso, Especialidad, Docente
from .models import Alumno, Contacto

# Búsqueda

def buscar_curso(request):
    busqueda = request.POST.get("buscar")
    cursos = Curso.objects.all()

    if busqueda:
        cursos = cursos.filter(
            nombre__icontains=busqueda
        )

    return render(request, 'BuscarCurso.html', {'cursos': cursos})

def buscar_docente(request):
    busqueda = request.POST.get("buscar")
    docentes = Docente.objects.all()

    if busqueda:
        docentes = docentes.filter(
            Q(nombre__icontains=busqueda) | 
            Q(apellido__icontains=busqueda) |
            Q(f_ingreso__icontains=busqueda)
        )

    return render(request, 'BuscarDocente.html', {'docentes': docentes})



def buscar_especialidad(request):
    busqueda = request.POST.get("buscar")
    especialidades = Especialidad.objects.all()

    if busqueda:
        especialidades = especialidades.filter(
            nombre__icontains=busqueda
        )

    return render(request, 'BuscarEspecialidad.html', {'especialidades': especialidades})

def buscar_alumno(request):
    busqueda = request.POST.get("buscar")
    alumnos = Alumno.objects.all()

    if busqueda:
        alumnos = alumnos.filter(
            nombre__icontains=busqueda
        )

    return render(request, 'BuscarAlumno.html', {'alumnos': alumnos})


def buscar_contacto(request):
    busqueda = request.POST.get("buscar")
    contactos = Contacto.objects.all()

    if busqueda:
        contactos = contactos.filter(
            apellido__icontains=busqueda
        )

    return render(request, 'BuscarContacto.html', {'contactos': contactos})



# Listado

def curso(request):
    cursosListado = Curso.objects.all()
    especialidades = Especialidad.objects.all()
    docentes = Docente.objects.all()
    return render(request, "GestionCursos.html", {"cursos": cursosListado, "especialidades": especialidades, "docentes": docentes})

def docente(request):
    docentes = Docente.objects.all()
    context = {'docentes': docentes}
    return render(request, 'GestionDocentes.html', context)

def especialidad(request):
    especialidades = Especialidad.objects.all()
    context = {'especialidades': especialidades}
    return render(request, 'GestionEspecialidades.html', context)


def alumno(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'GestionAlumnos.html', context)

def contacto(request):
    contactos = Contacto.objects.all()
    context = {'contactos': contactos}
    return render(request, 'GestionContactos.html', context)


# Registro

def registrarcurso(request):
    codigo = request.POST["codigo"]
    nombre = request.POST["nombre"]
    creditos = request.POST["creditos"]
    especialidad_id = request.POST["especialidad"]
    docente_id = request.POST["docente"]
    
    especialidad = Especialidad.objects.get(id=especialidad_id)
    docente = Docente.objects.get(id=docente_id)
    
    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, especialidad=especialidad, docente=docente)
    
    return redirect('/curso')

def registrardocente(request):
    apellido = request.POST["txtapellido"]
    nombre = request.POST["txtnombre"]
    fingreso_str = request.POST["txtfingreso"]
    dni = request.POST["txtdni"]
    telefono = request.POST["txttelefono"]
    
    fingreso = datetime.strptime(fingreso_str, "%Y-%m-%d").date()
    
    docente = Docente.objects.create(apellido=apellido, nombre=nombre, f_ingreso=fingreso, dni=dni, telefono=telefono)
    return redirect('/docente')

def registrarespecialidad(request):
    nombre = request.POST["txtnombre"]
    descripcion = request.POST["txtdescripcion"]
    
    especialidad = Especialidad.objects.create(nombre=nombre, descripcion=descripcion)
    return redirect('/especialidad')

def registrar_alumno(request):
    id_alumno = request.POST["txtid_alumno"]
    apellido = request.POST["txtapellido"]
    nombre = request.POST["txtnombre"]
    dni = request.POST["txtdni"]
    fechanacimiento_str = request.POST["txtfechanacimiento"]
    telefono = request.POST["txttelefono"]

    fechanacimiento = datetime.strptime(fechanacimiento_str, "%Y-%m-%d").date()
    
    alumno = Alumno.objects.create(
        id_alumno=id_alumno,
        apellido=apellido,
        nombre=nombre,
        dni=dni,
        fecha_nacimiento= fechanacimiento,
        telefono=telefono
    ) 
    return redirect('/alumno')



def registrar_contacto(request):
    codigo = request.POST['txtCodigo']
    foto = request.FILES.get('foto')
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    email = request.POST['txtEmail']
    fecha_nacimiento = request.POST['txtFecha_nacimiento']
    
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    
    contacto = Contacto.objects.create(
            codigo=codigo,
            foto=foto,
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            email=email
            
        )

    return redirect('/contacto')

# Eliminar

def eliminarcurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/curso')

def eliminardocente(request, id):
    docente = Docente.objects.get(id=id)
    docente.delete()
    return redirect('/docente')

def eliminarespecialidad(request, nombre):
    especialidad = Especialidad.objects.get(nombre=nombre)
    especialidad.delete()
    return redirect('/especialidad')

def eliminar_alumno(request, id_alumno):
    alumno = Alumno.objects.get(id_alumno=id_alumno)
    alumno.delete()
    return redirect('/alumno')

def eliminar_contacto(request, codigo):
    contacto = Contacto.objects.get(codigo=codigo)
    contacto.delete()
    return redirect('/contacto')


# Edición

def edicioncurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    cursoListado = Curso.objects.all()
    especialidades = Especialidad.objects.all()
    docentes = Docente.objects.all()
    return render(request, "EdicionCurso.html", {"curso": curso, "cursos": cursoListado, "especialidades": especialidades, "docentes": docentes})

def ediciondocente(request, id):
    docente = Docente.objects.get(id=id)
    return render(request, "EdicionDocente.html", {"docente": docente})

def edicionespecialidad(request, nombre):
    especialidad = Especialidad.objects.get(nombre=nombre)
    return render(request, "EdicionEspecialidad.html", {"especialidad": especialidad})

def edicionalumno(request, id_alumno):
    alumno = Alumno.objects.get(id_alumno=id_alumno)
    return render(request, "EdicionAlumno.html", {"alumno": alumno})


def edicion_contacto(request, codigo):
    contacto = Contacto.objects.get(codigo=codigo)
    return render(request, "EdicionContacto.html", {"contacto": contacto})


# Editar

def editarcurso(request, codigo):
    if request.method == "POST":
        nombre = request.POST["txtnombre"]
        creditos = request.POST["txtcreditos"]
        especialidad_id = request.POST["txtespecialidad"]
        docente_id = request.POST["txtdocente"]
        
        curso = Curso.objects.get(codigo=codigo)
        curso.nombre = nombre
        curso.creditos = creditos
        curso.especialidad_id = especialidad_id
        curso.docente_id = docente_id
        curso.save()
        
        return redirect('/curso')
    else:
        curso = Curso.objects.get(codigo=codigo)
        especialidades = Especialidad.objects.all()
        docentes = Docente.objects.all()
        return render(request, "EdicionCurso.html", {"curso": curso, "especialidades": especialidades, "docentes": docentes})



def editardocente(request, id):
    if request.method == "POST":
        apellido = request.POST["apellido"]
        nombre = request.POST["nombre"]
        f_ingreso_str = request.POST["f_ingreso"]
        dni = request.POST["dni"]
        telefono = request.POST["telefono"]
        
        f_ingreso = datetime.strptime(f_ingreso_str, "%Y-%m-%d").date()
        
        docente = Docente.objects.get(id=id)
        docente.apellido = apellido
        docente.nombre = nombre
        docente.f_ingreso = f_ingreso
        docente.dni = dni
        docente.telefono = telefono
        docente.save()
        
        return redirect('/docente')
    else:
        docente = Docente.objects.get(id=id)
        return render(request, "EdicionDocente.html", {"docente": docente})


def editarespecialidad(request, especialidad_id):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        
        especialidad = Especialidad.objects.get(id=especialidad_id)
        especialidad.nombre = nombre
        especialidad.descripcion = descripcion
        especialidad.save()
        
        return redirect('/especialidad')
    else:
        return redirect('/especialidad')
    

def editaralumno(request, id_alumno):
    if request.method == "POST":
        apellido = request.POST["txtapellido"]
        nombre = request.POST["txtnombre"]
        dni = request.POST["txtdni"]
        fecha_nacimiento = request.POST["txtfecha_nacimiento"]
        telefono = request.POST["txttelefono"]
        
        alumno = Alumno.objects.get(id_alumno=id_alumno)
        alumno.apellido = apellido
        alumno.nombre = nombre
        alumno.dni = dni
        alumno.fecha_nacimiento = fecha_nacimiento
        alumno.telefono = telefono
        alumno.save()
        
        return redirect('/alumno')
    else:
        alumno = Alumno.objects.get(id_alumno=id_alumno)
        return render(request, "EdicionAlumno.html", {"alumno": alumno})



def editar_contacto(request, codigo):
    if request.method == "POST":
        nombre = request.POST["txtNombre"]
        apellido = request.POST["txtApellido"]
        email = request.POST["txtEmail"]
        fecha_nacimiento = request.POST["txtFecha_nacimiento"]

        contacto = Contacto.objects.get(codigo=codigo)
        contacto.nombre = nombre
        contacto.apellido = apellido
        contacto.email = email
        contacto.fecha_nacimiento = fecha_nacimiento

        foto = request.FILES.get('foto')
        if foto:
            contacto.foto = foto

        contacto.save()

        return redirect('/contacto')
    else:
        contacto = Contacto.objects.get(codigo=codigo)
        return render(request, "EdicionContacto.html", {"contacto": contacto})

# vistas de login y demas, mas no de las tablas empleadas

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'Signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'Signup.html', {'form': form})
   
def homes(request): 
    return render(request, 'Home.html')
   
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'Home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'Login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'Login.html', {'form': form})
  
def profile(request): 
    return render(request, 'Profile.html')
   
def signout(request):
    logout(request)
    return redirect('/')


