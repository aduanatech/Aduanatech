# aranceles/admin.py
from django.contrib import admin
from .models import Arancel
# ... (Tu registro de Arancel sigue arriba) ...

class NotaExplicativaAdmin(admin.ModelAdmin):
    list_display = ('capitulo', 'titulo')
    search_fields = ('capitulo', 'titulo', 'contenido')