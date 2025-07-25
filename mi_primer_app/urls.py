from django.urls import path

from .views import (saludo, saludo_con_template, inicio, crear_repuesto, buscar_repuesto, 
                    listar_repuestos, crear_cliente, crear_unidad, AccesorioListView,
                    AccesorioCreateview, AccesorioDetailView, AccesorioUpdateView, AccesorioDeleteView, 
                    IndumentariaListView, IndumentariaCreateview, 
                    RepuestoDetailView, RepuestoUpdateView, RepuestoDeleteView,
                    IndumentariaDeleteView, IndumentariaDetailView, IndumentariaUpdateView, about )

urlpatterns = [
    path('', inicio, name='inicio'),
    path('saludo/', saludo, name='saludo'),
    path('hola-mundo-template/', saludo_con_template),
    path('about/', about, name='about'),
    path('crear-repuesto/', crear_repuesto, name='crear-repuesto'),
    path('repuestos/', listar_repuestos, name='repuesto'),
    path('repuestos/buscar', buscar_repuesto, name='buscar-repuesto'),
    path('crear-cliente/', crear_cliente, name='crear-cliente'),
    path('crear-unidad/', crear_unidad, name='crear-unidad'),

    # urls con vistas basadas ern clase
    
    #repuestos
    path('detalle-repuesto/<int:pk>', RepuestoDetailView.as_view(), name='detalle-repuesto'),
    path('editar-repuesto/<int:pk>', RepuestoUpdateView.as_view(), name='editar-repuesto'),
    path('eliminar-repuesto/<int:pk>', RepuestoDeleteView.as_view(), name='eliminar-repuesto'),

    #accesorios
    path('listar-accesorio/', AccesorioListView.as_view(), name='listar-accesorio'),
    path('crear-accesorio/', AccesorioCreateview.as_view(), name='crear-accesorio'),
    path('detalle-accesorio/<int:pk>', AccesorioDetailView.as_view(), name='detalle-accesorio'),
    path('editar-accesorio/<int:pk>', AccesorioUpdateView.as_view(), name='editar-accesorio'),
    path('eliminar-accesorio/<int:pk>', AccesorioDeleteView.as_view(), name='eliminar-accesorio'),

    #indumentaria
    path('listar-indumentaria/', IndumentariaListView.as_view(), name='listar-indumentaria'),
    path('crear-indumentaria/', IndumentariaCreateview.as_view(), name='crear-indumentaria'),
    path('detalle-indumentaria/<int:pk>', IndumentariaDetailView.as_view(), name='detalle-indumentaria'),
    path('editar-indumentaria/<int:pk>', IndumentariaUpdateView.as_view(), name='editar-indumentaria'),
    path('eliminar-indumentaria/<int:pk>', IndumentariaDeleteView.as_view(), name='eliminar-indumentaria')
    ]

