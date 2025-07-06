from django.urls import path

from .views import saludo, saludo_con_template, inicio, crear_repuesto, buscar_repuesto, listar_repuestos, crear_cliente, crear_unidad

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/', saludo, name='saludo'),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-repuesto/', crear_repuesto, name='crear-repuesto'),
    path('repuestos/', listar_repuestos, name='repuesto'),
    path('repuesto/buscar', buscar_repuesto, name='buscar-repuesto'),
    path('crear-cliente/', crear_cliente, name='crear-cliente'),
    path('crear-unidad/', crear_unidad, name='crear-unidad'),
]
