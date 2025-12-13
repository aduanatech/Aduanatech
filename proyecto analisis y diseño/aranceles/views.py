# aranceles/views.py
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required # Importar login_required
from .models import Arancel, ReporteError # <--- AGREGAR ReporteError
from .forms import (
    BusquedaArancelForm, ArancelForm, CargaMasivaForm,
    EliminarArancelForm, BuscarCodigoForm, ReporteErrorForm
)

# Importamos Modelos y TODOS los Formularios
from .models import Arancel
from .forms import BusquedaArancelForm, ArancelForm, CargaMasivaForm, EliminarArancelForm, BuscarCodigoForm

# ==========================================
#  SECCIÓN 1: PÚBLICA (Búsqueda y PDF)
# ==========================================

def buscar_arancel(request):
    """
    Vista pública. Busca EXACTAMENTE lo que escribes, respetando los puntos.
    """
    form = BusquedaArancelForm(request.GET or None)
    resultados = []
    mensaje = ""

    # 1. Si no hay búsqueda, mostrar los primeros 20
    if not request.GET:
        resultados = Arancel.objects.all()[:20]
    
    elif form.is_valid():
        query = form.cleaned_data['query'].strip()
        tipo = form.cleaned_data['tipo_busqueda']

        if query:
            # --- BÚSQUEDA POR DESCRIPCIÓN ---
            if tipo == 'descripcion':
                resultados = Arancel.objects.filter(descripcion__icontains=query).order_by('codigo')

            # --- BÚSQUEDA POR CÓDIGO ---
            elif tipo in ['capitulo', 'partida', 'sub_int', 'sub_reg', 'exacto']:
                # CORRECCIÓN: Usamos 'query' directamente para respetar los puntos (ej: 0303.41.00.00)
                resultados = Arancel.objects.filter(codigo__startswith=query).order_by('codigo')

            if not resultados:
                mensaje = f"No se encontraron resultados para '{query}'."

    return render(request, 'aranceles/buscar.html', {
        'form': form,
        'resultados': resultados,
        'mensaje': mensaje
    })

def detalle_arancel(request, pk):
    arancel = get_object_or_404(Arancel, pk=pk)
    return render(request, 'aranceles/detalle.html', {'arancel': arancel})

def exportar_aranceles_pdf(request):
    # Recibimos los mismos parámetros que la búsqueda
    query = request.GET.get('query', '').strip()
    tipo = request.GET.get('tipo_busqueda', '')
    resultados = []

    if query:
        if tipo == 'descripcion':
            resultados = Arancel.objects.filter(descripcion__icontains=query).order_by('codigo')
        else:
            # CORRECCIÓN AQUÍ TAMBIÉN: 
            # Quitamos el .replace(".", "") para que el PDF también encuentre los códigos con puntos
            resultados = Arancel.objects.filter(codigo__startswith=query).order_by('codigo')

    template_path = 'aranceles/pdf_template.html'
    context = {'resultados': resultados, 'query': query}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_aranceles.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Tuvimos errores al generar el PDF <pre>' + html + '</pre>')
    
    return response

# ==========================================
#  SECCIÓN 2: GESTIÓN ADMINISTRATIVA (CU-6)
#  (Esta sección se mantiene INTALTA para no romper nada)
# ==========================================

@staff_member_required
def menu_gestion_aranceles(request):
    """Menú principal con los botones."""
    return render(request, 'aranceles/menu_gestion.html')

@staff_member_required
def crear_arancel(request):
    """Opción 1: Crear manualmente."""
    if request.method == 'POST':
        form = ArancelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Arancel creado exitosamente!")
            return redirect('menu_gestion')
    else:
        form = ArancelForm()
    return render(request, 'aranceles/gestion_crear.html', {'form': form})

@staff_member_required
def actualizar_masivo(request):
    """Opción 2: Carga masiva (Excel o CSV)."""
    if request.method == 'POST':
        form = CargaMasivaForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            nombre_archivo = archivo.name.lower()
            
            try:
                # Detección de formato
                if nombre_archivo.endswith('.csv'):
                    df = pd.read_csv(archivo, engine='python', encoding='utf-8')
                elif nombre_archivo.endswith(('.xls', '.xlsx')):
                    df = pd.read_excel(archivo)
                else:
                    messages.error(request, "Formato no soportado. Use .csv o .xlsx")
                    return render(request, 'aranceles/gestion_actualizar.html', {'form': form})

                # Normalizar columnas a mayúsculas
                df.columns = [str(col).upper().strip() for col in df.columns]
                columnas_necesarias = ['CODIGO', 'DESCRIPCION', 'GRAVAMEN']
                
                if not all(col in df.columns for col in columnas_necesarias):
                    messages.error(request, f"Faltan columnas. El archivo debe tener: {', '.join(columnas_necesarias)}")
                    return render(request, 'aranceles/gestion_actualizar.html', {'form': form})

                contador = 0
                for index, row in df.iterrows():
                    codigo = str(row['CODIGO']).strip()
                    desc = str(row['DESCRIPCION']) 
                    
                    # Manejo de celdas vacías en Gravamen
                    grav = row['GRAVAMEN']
                    if pd.isna(grav) or grav == '':
                        grav = 0 

                    Arancel.objects.update_or_create(
                        codigo=codigo,
                        defaults={
                            'descripcion': desc,
                            'gravamen': grav,
                        }
                    )
                    contador += 1
                
                messages.success(request, f'Se procesaron {contador} aranceles correctamente.')
                return redirect('menu_gestion')

            except Exception as e:
                messages.error(request, f"Error al leer el archivo: {e}")
    else:
        form = CargaMasivaForm()

    return render(request, 'aranceles/gestion_actualizar.html', {'form': form})

@staff_member_required
def eliminar_arancel(request):
    """Opción 3: Eliminar por código."""
    arancel_encontrado = None
    
    if request.method == 'POST':
        if 'confirmar_eliminar' in request.POST:
            pk = request.POST.get('pk_eliminar')
            arancel = get_object_or_404(Arancel, pk=pk)
            codigo_borrado = arancel.codigo
            arancel.delete()
            messages.success(request, f"El arancel {codigo_borrado} fue eliminado.")
            return redirect('menu_gestion')
            
        form = EliminarArancelForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            try:
                arancel_encontrado = Arancel.objects.get(codigo=codigo)
            except Arancel.DoesNotExist:
                messages.error(request, f"No existe ningún arancel con el código {codigo}")
    else:
        form = EliminarArancelForm()

    return render(request, 'aranceles/gestion_eliminar.html', {
        'form': form, 
        'arancel': arancel_encontrado
    })
    
@staff_member_required
def buscar_para_editar(request):
    """Paso 1: Pantalla para buscar qué código queremos corregir"""
    if request.method == 'POST':
        form = BuscarCodigoForm(request.POST)
        if form.is_valid():
            codigo = form.cleaned_data['codigo']
            try:
                arancel = Arancel.objects.get(codigo=codigo)
                return redirect('realizar_edicion', pk=arancel.pk)
            except Arancel.DoesNotExist:
                messages.error(request, f"No se encontró el código {codigo}")
    else:
        form = BuscarCodigoForm()
    
    return render(request, 'aranceles/gestion_buscar_editar.html', {'form': form})

@staff_member_required
def realizar_edicion(request, pk):
    """Paso 2: Formulario con los datos cargados para corregirlos"""
    arancel = get_object_or_404(Arancel, pk=pk)
    
    if request.method == 'POST':
        form = ArancelForm(request.POST, instance=arancel)
        if form.is_valid():
            form.save()
            messages.success(request, f"¡El arancel {arancel.codigo} fue modificado exitosamente!")
            return redirect('menu_gestion')
    else:
        form = ArancelForm(instance=arancel)
    
    return render(request, 'aranceles/gestion_editar.html', {
        'form': form, 
        'arancel': arancel
    })
    
@login_required # Cualquier usuario logueado puede reportar
def crear_reporte_error(request):
    if request.method == 'POST':
        # Importante: request.FILES es necesario para subir archivos
        form = ReporteErrorForm(request.POST, request.FILES)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.usuario = request.user # Asignamos el usuario actual automáticamente
            reporte.save()
            messages.success(request, "¡Tu reporte ha sido enviado exitosamente!")
            return redirect('home') # Redirige al inicio
    else:
        form = ReporteErrorForm()
    
    return render(request, 'aranceles/reportes/crear_reporte.html', {'form': form})

@staff_member_required # Solo el administrador puede ver esto
def listar_reportes_admin(request):
    # Obtenemos todos los reportes ordenados por fecha
    reportes = ReporteError.objects.all()
    return render(request, 'aranceles/reportes/listar_reportes_admin.html', {'reportes': reportes})

@staff_member_required
def marcar_reporte_resuelto(request, pk):
    """Cambia el estado de un reporte a 'resuelto'"""
    reporte = get_object_or_404(ReporteError, pk=pk)
    
    # Cambiamos el estado
    reporte.estado = 'resuelto'
    reporte.save()
    
    messages.success(request, f"¡El reporte #{reporte.pk} ha sido marcado como RESUELTO!")
    return redirect('listar_reportes_admin')