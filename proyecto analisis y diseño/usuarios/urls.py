from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario_admin, name='crear_usuario_admin'),
    path('cambiar-rol/<int:user_id>/', views.cambiar_rol, name='cambiar_rol'),
    path('eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]