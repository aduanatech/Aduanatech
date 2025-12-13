# usuarios/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

# 1. VISTA: LISTA DE USUARIOS (Solo para Admins)
@staff_member_required
def lista_usuarios(request):
    # Traemos todos los usuarios del sistema
    users = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'users': users})

# 2. VISTA: CREAR USUARIO DESDE EL PANEL (Solo para Admins)
@staff_member_required
def crear_usuario_admin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('lista_usuarios')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/registro_admin.html', {'form': form})

# 3. VISTA: CAMBIAR ROL (Ascender/Degradar)
@staff_member_required
def cambiar_rol(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    
    # Regla de seguridad: No puedes quitarte el admin a ti mismo
    if usuario == request.user:
        messages.error(request, "No puedes cambiar tu propio rol.")
        return redirect('lista_usuarios')

    # Si es Admin (is_staff), lo volvemos normal. Si es normal, lo hacemos Admin.
    if usuario.is_staff:
        usuario.is_staff = False
        usuario.save()
        messages.warning(request, f'{usuario.username} ahora es DESPACHANTE.')
    else:
        usuario.is_staff = True
        usuario.save()
        messages.success(request, f'{usuario.username} ahora es ADMINISTRADOR.')
    
    return redirect('lista_usuarios')

# 4. VISTA: ELIMINAR USUARIO
@staff_member_required
def eliminar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    
    if usuario == request.user:
        messages.error(request, "No puedes eliminarte a ti mismo.")
    else:
        usuario.delete()
        messages.success(request, "Usuario eliminado.")
        
    return redirect('lista_usuarios')