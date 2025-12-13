# aranceles/models.py

from django.db import models
from django.contrib.auth.models import User

class Arancel(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    gravamen = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    
    # Campos adicionales (Regulaciones y Requisitos)
    ice_iehd = models.CharField(max_length=50, null=True, blank=True)
    unidad_medida = models.CharField(max_length=10, null=True, blank=True)
    despacho_frontera = models.BooleanField(null=True, blank=True)
    tipo_doc = models.CharField(max_length=20, null=True, blank=True)
    entidad_emite = models.CharField(max_length=100, null=True, blank=True)
    disp_legal = models.CharField(max_length=100, null=True, blank=True)
    
    # Preferencias Arancelarias (Enteros para porcentajes)
    pref_can_ace = models.IntegerField(null=True, blank=True)
    pref_ace22_chi = models.IntegerField(null=True, blank=True)
    pref_ace22_prot = models.IntegerField(null=True, blank=True)
    pref_ace66_mexico = models.IntegerField(null=True, blank=True)

    # --- CAMPO DE NOTAS EXPLICATIVAS ---
    nota_explicativa = models.TextField(
        null=True, 
        blank=True, 
        verbose_name="Nota Explicativa (OMA)",
        help_text="Texto oficial detallado de la Nota Explicativa para clasificar correctamente."
    )

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

class ReporteError(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('revisado', 'En Revisión'),
        ('resuelto', 'Resuelto'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Reportado por")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora")
    motivo = models.TextField(verbose_name="Descripción del Error")
    
    # FileField permite subir cualquier tipo de archivo (foto, video, pdf, etc.)
    archivo_adjunto = models.FileField(
        upload_to='reportes_adjuntos/', 
        null=True, 
        blank=True, 
        verbose_name="Foto o Video Adjunto"
    )
    
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    class Meta:
        ordering = ['-fecha_creacion'] # Ordenar del más reciente al más antiguo

    def __str__(self):
        return f"Reporte #{self.pk} - {self.usuario.username} - {self.estado}"