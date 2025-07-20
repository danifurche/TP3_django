from django import forms
from .models import Accesorio, Repuesto, Cliente, Unidad, Indumentaria

class RepuestoForm(forms.Form):
    num_parte = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    importe = forms.IntegerField(min_value=1, initial=10)
    activo = forms.BooleanField(required=False, initial=True)


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    celular = forms.CharField(max_length=20)
    email = forms.EmailField()
    fecha_cumple = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))


class UnidadForm(forms.Form):
    marca = forms.CharField(max_length=100)
    modelo = forms.CharField(max_length=100)
    anio = forms.IntegerField(min_value=1900, max_value=2100)

class AccesorioForm(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = ['num_parte', 'marca', 'descripcion']

class IndumentariaForm(forms.ModelForm):
    class Meta:
        model = Indumentaria
        fields = ['num_parte', 'marca', 'descripcion']

