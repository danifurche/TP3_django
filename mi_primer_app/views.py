from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Repuesto, Cliente, Unidad, Accesorio, Indumentaria

from .forms import RepuestoForm, ClienteForm, UnidadForm, AccesorioForm, IndumentariaForm

from django.http import HttpResponse

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')


def saludo(request):
    return HttpResponse("¡Hola, mundo!")

def about(request):
    return render(request, 'mi_primer_app/about.html')

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

@login_required
def crear_repuesto(request):
    if request.method == 'POST':
        form = RepuestoForm(request.POST)
        if form.is_valid():
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

def listar_repuestos(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'mi_primer_app/repuesto.html', {'repuestos': repuestos})

class RepuestoDetailView (DetailView):
    model = Repuesto
    template_name = 'mi_primer_app/detalle_Repuesto.html'
    context_object_name = 'repuesto'    

class RepuestoUpdateView (LoginRequiredMixin, UpdateView):
    model = Repuesto
    form_class = RepuestoForm
    template_name = 'mi_primer_app/crear_repuesto.html'
    success_url = reverse_lazy('listar-repuestos')

class RepuestoDeleteView (LoginRequiredMixin, DeleteView):
    model = Repuesto
    template_name = 'mi_primer_app/eliminar_repuesto.html'
    success_url = reverse_lazy('repuesto')

def buscar_repuesto(request):
    if request.method == 'GET':
        num_parte = request.GET.get('num_parte', '')
        resultados = Repuesto.objects.filter(num_parte__icontains=num_parte)
        return render(request, 'mi_primer_app/repuesto.html', {
            'repuestos': resultados,
            'num_parte': num_parte
        })

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            nuevo_cliente = Cliente(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                celular=form.cleaned_data['celular'],
                email=form.cleaned_data['email'],
                fecha_cumple=form.cleaned_data['fecha_cumple']
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

class AccesorioListView(ListView):
    model = Accesorio
    template_name = 'mi_primer_app/listar_accesorio.html'
    context_object_name = 'accesorio'
    ordering = ['num_parte']

    def get_queryset(self):
        queryset = super().get_queryset()
        num_parte = self.request.GET.get('num_parte')
        if num_parte:
            queryset = queryset.filter(num_parte__icontains=num_parte)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_parte'] = self.request.GET.get('num_parte', '')
        return context


class AccesorioCreateview(LoginRequiredMixin, CreateView):
    model = Accesorio
    form_class = AccesorioForm
    template_name = 'mi_primer_app/crear_accesorio.html'
    success_url = reverse_lazy('listar-accesorio')

class AccesorioDetailView (DetailView):
    model = Accesorio
    template_name = 'mi_primer_app/detalle_Accesorio.html'
    context_object_name = 'accesorio'    

class AccesorioUpdateView (LoginRequiredMixin, UpdateView):
    model = Accesorio
    form_class = AccesorioForm
    template_name = 'mi_primer_app/crear_accesorio.html'
    success_url = reverse_lazy('listar-accesorio')

class AccesorioDeleteView (LoginRequiredMixin, DeleteView):
    model = Accesorio
    template_name = 'mi_primer_app/eliminar_accesorio.html'
    success_url = reverse_lazy('listar-accesorio')

class IndumentariaListView(ListView):
    model = Indumentaria
    template_name = 'mi_primer_app/listar_indumentaria.html'
    context_object_name = 'indumentaria'
    ordering = ['num_parte']

    def get_queryset(self):
        queryset = super().get_queryset()
        num_parte = self.request.GET.get('num_parte')
        if num_parte:
            queryset = queryset.filter(num_parte__icontains=num_parte)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_parte'] = self.request.GET.get('num_parte', '')
        return context

class IndumentariaCreateview(LoginRequiredMixin, CreateView):
    model = Indumentaria
    form_class = IndumentariaForm
    template_name = 'mi_primer_app/crear_indumentaria.html'
    success_url = reverse_lazy('listar-indumentaria')

class IndumentariaDetailView (DetailView):
    model = Indumentaria
    template_name = 'mi_primer_app/detalle_indumentaria.html'
    context_object_name = 'indumentaria'    


class IndumentariaUpdateView (LoginRequiredMixin, UpdateView):
    model = Indumentaria
    form_class = IndumentariaForm
    template_name = 'mi_primer_app/crear_indumentaria.html'
    success_url = reverse_lazy('listar-indumentaria')

class IndumentariaDeleteView (LoginRequiredMixin, DeleteView):
    model = Indumentaria
    template_name = 'mi_primer_app/eliminar_indumentaria.html'
    success_url = reverse_lazy('listar-indumentaria')
