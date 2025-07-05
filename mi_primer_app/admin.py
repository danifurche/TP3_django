from django.contrib import admin

# Register your models here.
from .models import Familiar, Repuesto, Estudiante

register_models = [Familiar, Repuesto, Estudiante]

admin.site.register(register_models)
