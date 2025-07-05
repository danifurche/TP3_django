from django.shortcuts import render, redirect

from .models import Familiar, Repuesto, Estudiante

from .forms import RepuestoForm, EstudianteForm

# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


def crear_familiar(request, nombre):
    if nombre is not None:
        # Creamos un nuevo objeto Familiar
        nuevo_familiar = Familiar(
            nombre=nombre,
            apellido="ApellidoEjemplo",
            edad=30,
            fecha_nacimiento="1993-01-01",
            parentesco="Primo"
        )
        nuevo_familiar.save()
    return render(request, "mi_primer_app/crear_familiar.html", {"nombre": nombre})


def crear_repuesto(request):

    if request.method == 'POST':
        form = RepuestoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_repuesto = Repuesto(
                num_parte=form.cleaned_data['num_parte'],
                descripcion=form.cleaned_data['descripcion'],
                importe=form.cleaned_data['importe'],
                activo=form.cleaned_data['activo']
            )
            nuevo_repuesto.save()
            return redirect('repuesto')
    else:
        form = RepuestoForm()
        return render(request, 'mi_primer_app/crear_repuesto.html', {'form': form})


def crear_estudiante(request):

    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            # Procesar el formulario y guardar el curso
            nuevo_curso = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
                fecha_inscripcion=form.cleaned_data['fecha_inscripcion']
            )
            nuevo_curso.save()
            return redirect('inicio')
    else:
        form = EstudianteForm()
        return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})


def Repuestos(request):
    cursos = Repuestos.objects.all()
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos})


def buscar_repuesto(request):
    if request.method == 'GET':
        num_parte = request.GET.get('num_parte', '')
        cursos = Repuestos.objects.filter(nombre__icontains=num_parte)
        return render(request, 'mi_primer_app/cursos.html', {'Repuestos': Repuestos, 'nombre': num_parte})
