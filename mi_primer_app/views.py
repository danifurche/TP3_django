from django.shortcuts import render, redirect

from .models import Repuesto, Cliente, Unidad

from .forms import RepuestoForm, ClienteForm, UnidadForm

# Create your views here.
from django.http import HttpResponse


def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")


def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')


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

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            nuevo_cliente = Cliente(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                celular=form.cleaned_data['celular'],
                email=form.cleaned_data['email']
            )
            nuevo_cliente.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'mi_primer_app/crear_cliente.html', {'form': form})


def crear_unidad(request):
    if request.method == 'POST':
        form = UnidadForm(request.POST)
        if form.is_valid():
            nueva_unidad = Unidad(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                anio=form.cleaned_data['anio']
            )
            nueva_unidad.save()
            return redirect('inicio')
    else:
        form = UnidadForm()
    return render(request, 'mi_primer_app/crear_unidad.html', {'form': form})


def listar_repuestos(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'mi_primer_app/repuestos.html', {'repuestos': repuestos})


def buscar_repuesto(request):
    if request.method == 'GET':
        num_parte = request.GET.get('num_parte', '')
        resultados = Repuesto.objects.filter(num_parte__icontains=num_parte)
        return render(request, 'mi_primer_app/repuesto.html', {
            'repuestos': resultados,
            'num_parte': num_parte
        })

