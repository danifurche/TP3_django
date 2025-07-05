from django.urls import path

from .views import saludo, saludo_con_template, crear_familiar, inicio, crear_repuesto, crear_estudiante, buscar_repuesto, Repuestos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/', saludo, name= 'saludo'),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/', crear_familiar),
    path('crear-repuesto/', crear_repuesto, name='crear-repuesto'),
    path('crear-estudiante/', crear_estudiante, name='crear-estudiante'),
    path('Repuestos/', Repuestos, name='repuesto'),
    path('repuesto/buscar', buscar_repuesto, name='buscar-repuesto'),
]
