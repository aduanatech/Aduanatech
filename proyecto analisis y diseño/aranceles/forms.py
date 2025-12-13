# aranceles/forms.py
from django import forms
from .models import Arancel
from .models import Arancel, ReporteError

# 1. FORMULARIO DEL BUSCADOR (Público)
class BusquedaArancelForm(forms.Form):
    OPCIONES_BUSQUEDA = [
        ('descripcion', 'Nombre / Descripción del producto'),
        ('capitulo', 'Capítulo (2 dígitos)'),
        ('partida', 'Partida (4 dígitos)'),
        ('sub_int', 'Subpartida Internacional (6 dígitos)'),
        ('sub_reg', 'Subpartida Regional (8 dígitos)'),
        ('exacto', 'Código Nacional Completo (10 dígitos)'),
    ]

    query = forms.CharField(
        label='Criterio de búsqueda', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese código o texto...'})
    )
    tipo_busqueda = forms.ChoiceField(
        label='Buscar por', 
        choices=OPCIONES_BUSQUEDA, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )

# 2. FORMULARIO PARA CREAR/EDITAR (Manual)
# aranceles/forms.py (Solo la clase ArancelForm)

class ArancelForm(forms.ModelForm):
    class Meta:
        model = Arancel
        fields = [
            'codigo', 'descripcion', 'gravamen', 'ice_iehd', 
            'unidad_medida', 'despacho_frontera',
            'tipo_doc', 'entidad_emite', 'disp_legal',
            'pref_can_ace', 'pref_ace22_chi', 'pref_ace22_prot', 'pref_ace66_mexico'
        ]
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

# 3. FORMULARIO PARA CARGA MASIVA
class CargaMasivaForm(forms.Form):
    archivo = forms.FileField(
        label='Selecciona el archivo (.xlsx o .csv)',
        help_text='Soporta Excel y CSV (separado por comas o punto y coma).'
    )

# 4. FORMULARIO PARA ELIMINAR
class EliminarArancelForm(forms.Form):
    codigo = forms.CharField(label='Código del Arancel a Eliminar', max_length=20)

class BuscarCodigoForm(forms.Form):
    codigo = forms.CharField(
        label='Ingrese el Código del Arancel a Modificar', 
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Ej: 0101.21.00'})
    )
    
class ReporteErrorForm(forms.ModelForm):
    class Meta:
        model = ReporteError
        fields = ['motivo', 'archivo_adjunto'] # Solo mostramos estos campos
        widgets = {
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe el error detalladamente...'}),
            'archivo_adjunto': forms.FileInput(attrs={'class': 'form-control'}),
        }