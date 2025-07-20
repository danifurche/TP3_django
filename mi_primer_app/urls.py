from django.urls import path

from .views import (saludo, saludo_con_template, inicio, crear_repuesto, buscar_repuesto, 
                    listar_repuestos, crear_cliente, crear_unidad, AccesorioListView,
                    AccesorioCreateview, AccesorioDetailView, AccesorioUpdateView, AccesorioDeleteView, 
                    IndumentariaListView, IndumentariaCreateview,
                    IndumentariaDeleteView, IndumentariaDetailView, IndumentariaUpdateView )

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/', saludo, name='saludo'),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-repuesto/', crear_repuesto, name='crear-repuesto'),
    path('repuestos/', listar_repuestos, name='repuesto'),
    path('repuestos/buscar', buscar_repuesto, name='buscar-repuesto'),
    path('crear-cliente/', crear_cliente, name='crear-cliente'),
    path('crear-unidad/', crear_unidad, name='crear-unidad'),

    # urls con vistas basadas ern clase
    path('listar-accesorio/', AccesorioListView.as_view(), name='listar-accesorio'),
    path('crear-accesorio/', AccesorioCreateview.as_view(), name='crear-accesorio'),
    path('detalle-accesorio/<int:pk>', AccesorioDetailView.as_view(), name='detalle-accesorio'),
    path('editar/<int:pk>', AccesorioUpdateView.as_view(), name='editar-accesorio'),
    path('eliminar/<int:pk>', AccesorioDeleteView.as_view(), name='eliminar-accesorio'),
    path('listar-indumentaria/', IndumentariaListView.as_view(), name='listar-indumentaria'),
    path('crear-indumentaria/', IndumentariaCreateview.as_view(), name='crear-indumentaria'),
    path('detalle-indumentaria/<int:pk>', IndumentariaDetailView.as_view(), name='detalle-indumentaria'),
    path('editar/<int:pk>', IndumentariaUpdateView.as_view(), name='editar-indumentaria'),
    path('eliminar/<int:pk>', IndumentariaDeleteView.as_view(), name='eliminar-indumentaria')
    ]

