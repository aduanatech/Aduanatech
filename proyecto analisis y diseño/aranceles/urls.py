# aranceles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rutas de Aranceles (CU-2 y CU-3)
    path('buscar/', views.buscar_arancel, name='buscar_arancel'),
    path('detalle/<int:pk>/', views.detalle_arancel, name='detalle_arancel'),
    path('exportar-pdf/', views.exportar_aranceles_pdf, name='exportar_pdf'),
    path('gestion/', views.menu_gestion_aranceles, name='menu_gestion'),
    path('gestion/crear/', views.crear_arancel, name='crear_arancel'),
    path('gestion/actualizar/', views.actualizar_masivo, name='actualizar_masivo'),
    path('gestion/eliminar/', views.eliminar_arancel, name='eliminar_arancel'),
    path('gestion/modificar-buscar/', views.buscar_para_editar, name='buscar_para_editar'),
    path('gestion/editar/<int:pk>/', views.realizar_edicion, name='realizar_edicion'),  
    path('reportar-error/', views.crear_reporte_error, name='crear_reporte_error'),
    path('gestion/reportes/', views.listar_reportes_admin, name='listar_reportes_admin'),
    path('gestion/reportes/resolver/<int:pk>/', views.marcar_reporte_resuelto, name='marcar_reporte_resuelto'),
]