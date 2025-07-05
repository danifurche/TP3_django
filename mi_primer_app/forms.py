from django import forms


class RepuestoForm(forms.Form):
    num_parte = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    importe = forms.IntegerField(min_value=1, initial=10)
    widget=forms.DateInput(attrs={'type': 'date'})
    activo = forms.BooleanField(required=False, initial=True)


class EstudianteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField()
    edad = forms.IntegerField(min_value=10, max_value=100)
    fecha_inscripcion = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
