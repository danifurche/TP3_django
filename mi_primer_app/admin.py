from django.contrib import admin

# Register your models here.
from .models import Repuesto

register_models = [Repuesto]

admin.site.register(register_models)
