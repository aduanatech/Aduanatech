from django.core.management.base import BaseCommand
from aranceles.models import Arancel

class Command(BaseCommand):
    help = 'Carga TODOS los productos (Caps 1-3) con campos extra en NONE para edición manual.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Limpiando base de datos...")
        Arancel.objects.all().delete()

        # ESTRUCTURA BASE PARA EDICIÓN MANUAL
        # codigo: STR | descripcion: STR | gravamen: INT/None
        # RESTO: None (Para que tú los llenes luego)

        datos = [
           {
        "codigo": "01.01", 
        "descripcion": "Caballos, asnos, mulos y burdéganos, vivos.", 
        "gravamen": None,
        "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "", 
            "descripcion": "   - Caballos:", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0101.21.00.00", 
            "descripcion": "      -- Reproductores de raza pura", 
            "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0101.29", 
            "descripcion": "      -- Los demás:", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0101.29.10.00", 
            "descripcion": "         --- Para carrera", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0101.29.90.00", 
            "descripcion": "         --- Los demás", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0101.30.00.00", 
            "descripcion": "   - Asnos", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0101.90.00.00", 
            "descripcion": "   - Los demás (mulos y burdéganos)", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "01.02", 
            "descripcion": "Animales vivos de la especie bovina.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0102.21.00.00", 
            "descripcion": "   - Reproductores de raza pura", 
            "gravamen": 0,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0102.29.10.00", 
            "descripcion": "   - Para lidia", 
            "gravamen": 0,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0102.29.90.00", 
            "descripcion": "   - Los demás", 
            "gravamen": 0,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0102.31.00.00", 
            "descripcion": "   - Búfalos: Reproductores de raza pura", 
            "gravamen": 0,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0102.39.00.00", 
            "descripcion": "   - Búfalos: Los demás", 
            "gravamen": 0,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0102.90.00.00", 
            "descripcion": "   - Los demás", 
            "gravamen": 0,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "01.03", 
            "descripcion": "Animales vivos de la especie porcina.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0103.10.00.00", 
            "descripcion": "   - Reproductores de raza pura", 
            "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0103.91.00.00", 
            "descripcion": "   - De peso inferior a 50 kg", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0103.92.00.00", 
            "descripcion": "   - De peso superior o igual a 50 kg", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "01.04", 
            "descripcion": "Animales vivos de las especies ovina o caprina.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0104.10.10.00", 
            "descripcion": "   - Ovinos: Reproductores de raza pura", 
            "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0104.10.90.00", 
            "descripcion": "   - Ovinos: Los demás", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0104.20.10.00", 
            "descripcion": "   - Caprinos: Reproductores de raza pura", 
            "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0104.20.90.00", 
            "descripcion": "   - Caprinos: Los demás", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "01.05", 
            "descripcion": "Gallos, gallinas, patos, gansos, pavos...", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0105.11.00.00", 
            "descripcion": "   - Gallus domesticus (peso <= 185g)", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0105.12.00.00", 
            "descripcion": "   - Pavos (gallipavos) (peso <= 185g)", 
            "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0105.13.00.00", 
            "descripcion": "   - Patos (peso <= 185g)", 
            "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0105.14.00.00", 
            "descripcion": "   - Gansos (peso <= 185g)", 
            "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0105.15.00.00", 
            "descripcion": "   - Pintadas (peso <= 185g)", 
            "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0105.94.00.00", 
            "descripcion": "   - Aves Gallus domesticus (peso > 185g)", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0105.99.00.00", 
            "descripcion": "   - Las demás aves", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "01.06", 
            "descripcion": "Los demás animales vivos.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.11.00.00", 
            "descripcion": "   - Primates", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.12.00.00", 
            "descripcion": "   - Ballenas, delfines, manatíes, etc.", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.13.11.10", 
            "descripcion": "      -- Llamas (Lama glama)", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.13.11.20", 
            "descripcion": "      -- Guanacos (Lama guanicoe)", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.13.12.00", 
            "descripcion": "      -- Alpacas (Lama pacos)", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.13.19.00", 
            "descripcion": "      -- Las demás vicuñas y camélidos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.13.90.00", 
            "descripcion": "      -- Los demás camélidos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.14.00.00", 
            "descripcion": "   - Conejos y liebres", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.19.00.10", 
            "descripcion": "   - Perros y gatos domésticos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.19.00.90", 
            "descripcion": "   - Los demás mamíferos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.20.00.00", 
            "descripcion": "   - Reptiles (incl. serpientes)", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.31.00.00", 
            "descripcion": "   - Aves de rapiña", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.32.00.00", 
            "descripcion": "   - Psitaciformes (loros, etc.)", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.33.00.00", 
            "descripcion": "   - Avestruces y emúes", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.39.00.00", 
            "descripcion": "   - Las demás aves", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.41.00.00", 
            "descripcion": "   - Abejas", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.49.00.00", 
            "descripcion": "   - Los demás insectos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0106.90.00.00", 
            "descripcion": "   - Los demás animales vivos", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "u", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "02.01", 
            "descripcion": "Carne de animales de la especie bovina, fresca.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0201.10.00.00", 
            "descripcion": "   - En canales o medias canales", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0201.20.00.00", 
            "descripcion": "   - Los demás cortes con hueso", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0201.30.00.10", 
            "descripcion": "   - Deshuesada: Trimming", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0201.30.00.90", 
            "descripcion": "   - Deshuesada: Las demás", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "02.02", 
            "descripcion": "Carne de animales de la especie bovina, congelada.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0202.10.00.00", 
            "descripcion": "   - En canales o medias canales", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0202.20.00.00", 
            "descripcion": "   - Los demás cortes con hueso", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0202.30.00.10", 
            "descripcion": "   - Deshuesada: Trimming", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0202.30.00.90", 
            "descripcion": "   - Deshuesada: Las demás", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "02.03", 
            "descripcion": "Carne de animales de la especie porcina.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.11.00.00", 
            "descripcion": "   - Fresca: En canales o medias canales", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.12.00.00", 
            "descripcion": "   - Fresca: Piernas, paletas y sus trozos", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.19.10.00", 
            "descripcion": "   - Fresca: Deshuesada", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.19.20.00", 
            "descripcion": "   - Fresca: Chuletas y costillas", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.19.30.00", 
            "descripcion": "   - Fresca: Tocino con partes magras", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.19.90.00", 
            "descripcion": "   - Fresca: Las demás", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.21.00.00", 
            "descripcion": "   - Congelada: En canales", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.22.00.00", 
            "descripcion": "   - Congelada: Piernas y paletas", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.29.10.00", 
            "descripcion": "   - Congelada: Deshuesada", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.29.20.00", 
            "descripcion": "   - Congelada: Chuletas y costillas", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.29.30.00", 
            "descripcion": "   - Congelada: Tocino con partes magras", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0203.29.90.00", 
            "descripcion": "   - Congelada: Las demás", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "02.04", 
            "descripcion": "Carne de animales de las especies ovina o caprina.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0204.10.00.00", 
            "descripcion": "   - Canales de cordero, frescas", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0204.21.00.00", 
            "descripcion": "   - Fresca: En canales o medias canales", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0204.22.00.00", 
            "descripcion": "   - Fresca: Cortes sin deshuesar", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0204.23.00.00", 
            "descripcion": "   - Fresca: Deshuesada", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0204.30.00.00", 
            "descripcion": "   - Canales de cordero, congeladas", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0204.41.00.00", 
            "descripcion": "   - Congelada: En canales", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0204.42.00.00", 
            "descripcion": "   - Congelada: Cortes sin deshuesar", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0204.43.00.00", 
            "descripcion": "   - Congelada: Deshuesada", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0204.50.00.00", 
            "descripcion": "   - Carne de caprinos", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0205.00.00.00", 
            "descripcion": "Carne de caballar, asnal o mular", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "02.06", 
            "descripcion": "Despojos comestibles.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.10.00.00", 
            "descripcion": "   - Bovinos, frescos o refrigerados", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.21.00.00", 
            "descripcion": "   - Lenguas bovinas congeladas", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.22.00.00", 
            "descripcion": "   - Hígados bovinos congelados", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.29.00.00", 
            "descripcion": "   - Los demás despojos bovinos", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.30.00.00", 
            "descripcion": "   - Porcinos, frescos o refrigerados", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.41.00.00", 
            "descripcion": "   - Hígados porcinos congelados", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.49.10.00", 
            "descripcion": "   - Piel comestible porcina", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.49.90.00", 
            "descripcion": "   - Los demás despojos porcinos", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.80.00.00", 
            "descripcion": "   - Los demás, frescos o refrigerados", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0206.90.00.00", 
            "descripcion": "   - Los demás, congelados", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "02.07", 
            "descripcion": "Carne y despojos de aves.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.11.00.00", 
            "descripcion": "   - Gallus domesticus: Sin trocear, frescos", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.12.00.00", 
            "descripcion": "   - Gallus domesticus: Sin trocear, congelados", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.13.00.00", 
            "descripcion": "   - Gallus domesticus: Trozos frescos", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.14.00.00", 
            "descripcion": "   - Gallus domesticus: Trozos congelados", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.24.00.00", 
            "descripcion": "   - Pavos: Sin trocear, frescos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.25.00.00", 
            "descripcion": "   - Pavos: Sin trocear, congelados", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.26.00.00", 
            "descripcion": "   - Pavos: Trozos frescos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.27.00.00", 
            "descripcion": "   - Pavos: Trozos congelados", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.41.00.00", 
            "descripcion": "   - Patos: Sin trocear, frescos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.42.00.00", 
            "descripcion": "   - Patos: Sin trocear, congelados", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.43.00.00", 
            "descripcion": "   - Patos: Hígados grasos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.44.00.00", 
            "descripcion": "   - Patos: Otros frescos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.45.00.00", 
            "descripcion": "   - Patos: Otros congelados", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.51.00.00", 
            "descripcion": "   - Gansos: Sin trocear, frescos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.52.00.00", 
            "descripcion": "   - Gansos: Sin trocear, congelados", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.53.00.00", 
            "descripcion": "   - Gansos: Hígados grasos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.54.00.00", 
            "descripcion": "   - Gansos: Otros frescos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.55.00.00", 
            "descripcion": "   - Gansos: Otros congelados", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0207.60.00.00", 
            "descripcion": "   - De pintada", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "02.08", 
            "descripcion": "Las demás carnes y despojos.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0208.10.00.00", 
            "descripcion": "   - De conejo o liebre", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0208.30.00.00", 
            "descripcion": "   - De primates", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0208.40.00.00", 
            "descripcion": "   - De ballenas, delfines y mamíferos marinos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0208.50.00.00", 
            "descripcion": "   - De reptiles", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0208.60.00.00", 
            "descripcion": "   - De camellos y camélidos", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0208.90.00.00", 
            "descripcion": "   - Las demás carnes", 
            "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "02.09", 
            "descripcion": "Tocino y grasa de cerdo o ave.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0209.10.10.00", 
            "descripcion": "   - Tocino sin partes magras", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0209.10.90.00", 
            "descripcion": "   - Grasa de cerdo sin fundir", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0209.90.00.00", 
            "descripcion": "   - Las demás grasas", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "02.10", 
            "descripcion": "Carne salada, seca o ahumada.", 
            "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0210.11.00.00", 
            "descripcion": "   - Jamones y paletas, salados", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0210.12.00.00", 
            "descripcion": "   - Tocino entreverado (panceta)", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0210.19.00.00", 
            "descripcion": "   - Las demás carnes porcinas", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0210.20.00.00", 
            "descripcion": "   - Carne bovina salada", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0210.91.00.00", 
            "descripcion": "   - De primates", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0210.92.00.00", 
            "descripcion": "   - De ballenas, delfines, etc.", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0210.93.00.00", 
            "descripcion": "   - De reptiles", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0210.99.10.00", 
            "descripcion": "   - Harina y polvo comestibles", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0210.99.90.00", 
            "descripcion": "   - Los demás", 
            "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "03.01", "descripcion": "Peces vivos.", "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.11.00.00", "descripcion": "   - Peces ornamentales de agua dulce", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.19.00.00", "descripcion": "   - Los demás peces ornamentales", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.91.10.00", "descripcion": "   - Truchas: Para reproducción", "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.91.90.00", "descripcion": "   - Las demás truchas vivas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.92.00.00", "descripcion": "   - Anguilas vivas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.93.00.00", "descripcion": "   - Carpas vivas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.94.00.00", "descripcion": "   - Atunes de aleta azul vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.95.00.00", "descripcion": "   - Atunes del sur vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.99.11.00", "descripcion": "   - Tilapia para reproducción", "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.99.19.10", "descripcion": "   - Paiche (Arapaima gigas) vivo", "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.99.19.90", "descripcion": "   - Los demás", "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0301.99.90.00", "descripcion": "   - Los demás peces vivos", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "03.02", "descripcion": "Pescado fresco o refrigerado.", "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.11.00.00", "descripcion": "   - Truchas frescas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.13.00.00", "descripcion": "   - Salmones del Pacífico", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.14.00.00", "descripcion": "   - Salmones del Atlántico", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.19.00.00", "descripcion": "   - Los demás salmónidos", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.21.00.00", "descripcion": "   - Fletanes frescos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.22.00.00", "descripcion": "   - Sollas frescas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.23.00.00", "descripcion": "   - Lenguados frescos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.24.00.00", "descripcion": "   - Rodaballos frescos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.29.00.00", "descripcion": "   - Los demás planos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.31.00.00", "descripcion": "   - Albacoras", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.32.00.00", "descripcion": "   - Atunes aleta amarilla", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.33.00.00", "descripcion": "   - Listados (bonitos)", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.34.00.00", "descripcion": "   - Patudos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.35.00.00", "descripcion": "   - Atunes aleta azul", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.36.00.00", "descripcion": "   - Atunes del sur", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.39.00.00", "descripcion": "   - Los demás atunes", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.41.00.00", "descripcion": "   - Arenques", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.42.00.00", "descripcion": "   - Anchoas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.43.00.00", "descripcion": "   - Sardinas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.44.00.00", "descripcion": "   - Caballas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.45.00.00", "descripcion": "   - Jureles", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.46.00.00", "descripcion": "   - Cobias", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.47.00.00", "descripcion": "   - Peces espada", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.49.00.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.51.00.00", "descripcion": "   - Bacalaos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.52.00.00", "descripcion": "   - Eglefinos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.53.00.00", "descripcion": "   - Carboneros", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.54.00.00", "descripcion": "   - Merluzas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.55.00.00", "descripcion": "   - Abadejos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.56.00.00", "descripcion": "   - Bacaladillas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.59.00.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.71.00.00", "descripcion": "   - Tilapias", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.72.00.00", "descripcion": "   - Bagres", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.73.00.00", "descripcion": "   - Carpas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.74.00.00", "descripcion": "   - Anguilas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.79.00.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.81.00.00", "descripcion": "   - Cazones y escualos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.82.00.00", "descripcion": "   - Rayas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.83.00.00", "descripcion": "   - Austromerluzas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.84.00.00", "descripcion": "   - Róbalos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.85.00.00", "descripcion": "   - Sargos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.89.00.10", "descripcion": "   - Paiche (Arapaima gigas)", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.89.00.90", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.91.00.00", "descripcion": "   - Hígados, huevas y lechas", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.92.00.00", "descripcion": "   - Aletas de tiburón", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.99.00.10", "descripcion": "   - Despojos de truchas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.99.00.20", "descripcion": "   - Despojos de salmónidos", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0302.99.00.90", "descripcion": "   - Los demás despojos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "03.03", "descripcion": "Pescado congelado.", "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.11.00.00", "descripcion": "   - Salmones rojos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.12.00.00", "descripcion": "   - Los demás salmones Pacífico", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.13.00.00", "descripcion": "   - Salmones Atlántico", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.14.00.00", "descripcion": "   - Truchas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.19.00.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.23.00.00", "descripcion": "   - Tilapias", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.24.00.00", "descripcion": "   - Bagres", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.25.00.00", "descripcion": "   - Carpas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.26.00.00", "descripcion": "   - Anguilas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.29.00.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.31.00.00", "descripcion": "   - Fletanes", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.32.00.00", "descripcion": "   - Sollas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.33.00.00", "descripcion": "   - Lenguados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.34.00.00", "descripcion": "   - Rodaballos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.39.00.00", "descripcion": "   - Los demás planos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.41.00.00", "descripcion": "   - Albacoras", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.42.00.00", "descripcion": "   - Atunes aleta amarilla", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.43.00.00", "descripcion": "   - Listados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.44.00.00", "descripcion": "   - Patudos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.45.00.00", "descripcion": "   - Atunes aleta azul", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.46.00.00", "descripcion": "   - Atunes del sur", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.49.00.00", "descripcion": "   - Los demás atunes", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.51.00.00", "descripcion": "   - Arenques", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.53.00.00", "descripcion": "   - Sardinas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.54.00.00", "descripcion": "   - Caballas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.55.00.00", "descripcion": "   - Jureles", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.56.00.00", "descripcion": "   - Cobias", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.57.00.00", "descripcion": "   - Peces espada", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.59.00.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.63.00.00", "descripcion": "   - Bacalaos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.64.00.00", "descripcion": "   - Eglefinos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.65.00.00", "descripcion": "   - Carboneros", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.66.00.00", "descripcion": "   - Merluzas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.67.00.00", "descripcion": "   - Abadejos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.68.00.00", "descripcion": "   - Bacaladillas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.69.00.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.81.00.00", "descripcion": "   - Cazones y escualos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.82.00.00", "descripcion": "   - Rayas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.83.00.00", "descripcion": "   - Austromerluzas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.84.00.00", "descripcion": "   - Róbalos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.89.00.10", "descripcion": "   - Paiche", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.89.00.90", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.91.00.00", "descripcion": "   - Hígados y huevas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.92.00.00", "descripcion": "   - Aletas de tiburón", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.99.00.10", "descripcion": "   - Despojos de truchas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0303.99.00.90", "descripcion": "   - Los demás despojos", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "03.04", "descripcion": "Filetes y carne de pescado.", "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.31.00.00", "descripcion": "   - Frescos: Tilapias", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.32.00.00", "descripcion": "   - Frescos: Bagres", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.33.00.00", "descripcion": "   - Frescos: Percas del Nilo", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.39.00.00", "descripcion": "   - Frescos: Los demás", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.41.00.00", "descripcion": "   - Frescos: Salmones", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.42.00.00", "descripcion": "   - Frescos: Truchas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.43.00.00", "descripcion": "   - Frescos: Planos", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.44.00.00", "descripcion": "   - Frescos: Gadidae", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.45.00.00", "descripcion": "   - Frescos: Pez espada", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.46.00.00", "descripcion": "   - Frescos: Austromerluzas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.47.00.00", "descripcion": "   - Frescos: Escualos", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.48.00.00", "descripcion": "   - Frescos: Rayas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.49.00.00", "descripcion": "   - Frescos: Los demás", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.51.00.00", "descripcion": "   - Frescos: Tilapias y bagres", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.52.00.00", "descripcion": "   - Frescos: Salmónidos", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.53.00.00", "descripcion": "   - Frescos: Gadidae", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.54.00.00", "descripcion": "   - Frescos: Pez espada", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.55.00.00", "descripcion": "   - Frescos: Austromerluzas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.56.00.00", "descripcion": "   - Frescos: Escualos", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.57.00.00", "descripcion": "   - Frescos: Rayas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.59.00.00", "descripcion": "   - Frescos: Los demás", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.61.00.00", "descripcion": "   - Congelados: Tilapia", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.62.00.00", "descripcion": "   - Congelados: Bagre", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.63.00.00", "descripcion": "   - Congelados: Perca del Nilo", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.69.00.00", "descripcion": "   - Congelados: Los demás", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.71.00.00", "descripcion": "   - Congelados: Bacalao", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.72.00.00", "descripcion": "   - Congelados: Eglefino", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.73.00.00", "descripcion": "   - Congelados: Carbonero", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.74.00.00", "descripcion": "   - Congelados: Merluza", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.75.00.00", "descripcion": "   - Congelados: Abadejo", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.79.00.00", "descripcion": "   - Congelados: Los demás", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.81.00.00", "descripcion": "   - Congelados: Salmón", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.82.00.00", "descripcion": "   - Congelados: Trucha", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.83.00.00", "descripcion": "   - Congelados: Planos", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.84.00.00", "descripcion": "   - Congelados: Pez espada", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.85.00.00", "descripcion": "   - Congelados: Austromerluzas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.86.00.00", "descripcion": "   - Congelados: Arenques", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.87.00.00", "descripcion": "   - Congelados: Atunes", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.88.00.00", "descripcion": "   - Congelados: Escualos", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.89.00.00", "descripcion": "   - Congelados: Los demás", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.91.00.00", "descripcion": "   - Congelados: Pez espada", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.92.00.00", "descripcion": "   - Congelados: Austromerluzas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.93.00.00", "descripcion": "   - Congelados: Tilapias y bagres", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.94.00.00", "descripcion": "   - Congelados: Abadejo", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.95.00.00", "descripcion": "   - Congelados: Gadidae", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.96.00.00", "descripcion": "   - Congelados: Escualos", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.97.00.00", "descripcion": "   - Congelados: Rayas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.99.00.10", "descripcion": "   - Congelados: Paiche", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0304.99.00.90", "descripcion": "   - Congelados: Los demás", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "03.05", "descripcion": "Pescado seco, salado o en salmuera.", "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.20.00.00", "descripcion": "   - Hígados y huevas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.31.00.00", "descripcion": "   - Filetes: Tilapia", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.32.00.00", "descripcion": "   - Filetes: Gadidae", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.39.10.00", "descripcion": "   - Filetes: Bacalao", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.39.90.10", "descripcion": "   - Filetes: Paiche", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.39.90.90", "descripcion": "   - Filetes: Los demás", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.41.00.00", "descripcion": "   - Ahumado: Salmones", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.42.00.00", "descripcion": "   - Ahumado: Arenques", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.43.00.00", "descripcion": "   - Ahumado: Truchas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.44.00.00", "descripcion": "   - Ahumado: Tilapias", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.49.00.00", "descripcion": "   - Ahumado: Los demás", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.51.00.00", "descripcion": "   - Seco: Bacalaos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.52.00.00", "descripcion": "   - Seco: Tilapias", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.53.10.00", "descripcion": "   - Seco: Merluzas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.53.90.00", "descripcion": "   - Seco: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.54.00.00", "descripcion": "   - Seco: Arenques, anchoas, etc.", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.59.00.00", "descripcion": "   - Seco: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.61.00.00", "descripcion": "   - Salado: Arenques", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.62.00.00", "descripcion": "   - Salado: Bacalaos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.63.00.00", "descripcion": "   - Salado: Anchoas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.64.00.00", "descripcion": "   - Salado: Tilapias", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.69.00.00", "descripcion": "   - Salado: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.71.00.10", "descripcion": "   - Aletas tiburón: Ahumadas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.71.00.90", "descripcion": "   - Aletas tiburón: Las demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.72.00.00", "descripcion": "   - Cabezas y colas", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.79.00.10", "descripcion": "   - Los demás: Ahumados", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0305.79.00.90", "descripcion": "   - Los demás: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "03.06", "descripcion": "Crustáceos.", "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.11.00.00", "descripcion": "   - Langostas congeladas", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.12.00.00", "descripcion": "   - Bogavantes congelados", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.14.00.00", "descripcion": "   - Cangrejos congelados", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.15.00.00", "descripcion": "   - Cigalas congeladas", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.16.00.00", "descripcion": "   - Camarones agua fría congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.17.11.00", "descripcion": "   - Langostinos: Enteros", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.17.12.00", "descripcion": "   - Langostinos: Colas sin caparazón", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.17.13.00", "descripcion": "   - Langostinos: Colas con caparazón", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.17.14.00", "descripcion": "   - Langostinos: Colas cocidas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.17.19.00", "descripcion": "   - Langostinos: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.17.91.00", "descripcion": "   - Camarones de río", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.17.99.00", "descripcion": "   - Los demás camarones", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.19.00.00", "descripcion": "   - Los demás", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.31.00.00", "descripcion": "   - Langostas vivas", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.32.00.00", "descripcion": "   - Bogavantes vivos", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.33.00.00", "descripcion": "   - Cangrejos vivos", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.34.00.00", "descripcion": "   - Cigalas vivas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.35.00.00", "descripcion": "   - Camarones agua fría vivos", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.36.11.00", "descripcion": "   - Langostinos para reproducción", "gravamen": 5,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.36.19.00", "descripcion": "   - Langostinos vivos", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.36.91.00", "descripcion": "   - Camarones río reproducción", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.36.92.00", "descripcion": "   - Camarones río vivos", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.36.99.00", "descripcion": "   - Los demás", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.39.00.00", "descripcion": "   - Los demás vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.91.00.00", "descripcion": "   - Langostas: Otros", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.92.00.00", "descripcion": "   - Bogavantes: Otros", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.93.00.00", "descripcion": "   - Cangrejos: Otros", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.94.00.00", "descripcion": "   - Cigalas: Otros", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.95.10.00", "descripcion": "   - Camarones río: Otros", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.95.90.00", "descripcion": "   - Los demás: Otros", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0306.99.00.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "03.07", "descripcion": "Moluscos.", "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.11.00.00", "descripcion": "   - Ostras vivas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.12.00.00", "descripcion": "   - Ostras congeladas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.19.00.00", "descripcion": "   - Ostras: Las demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.21.10.00", "descripcion": "   - Vieiras: Pecten jacobaeus", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.21.90.00", "descripcion": "   - Vieiras: Las demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.22.10.00", "descripcion": "   - Congeladas: Pecten jacobaeus", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.22.90.00", "descripcion": "   - Congeladas: Las demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.29.10.00", "descripcion": "   - Otras: Pecten jacobaeus", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.29.90.00", "descripcion": "   - Otras: Las demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.31.00.00", "descripcion": "   - Mejillones vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.32.00.00", "descripcion": "   - Mejillones congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.39.00.00", "descripcion": "   - Mejillones: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.42.00.00", "descripcion": "   - Jibias y calamares vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.43.00.00", "descripcion": "   - Jibias y calamares congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.49.00.00", "descripcion": "   - Jibias y calamares: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.51.00.00", "descripcion": "   - Pulpos vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.52.00.00", "descripcion": "   - Pulpos congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.59.00.00", "descripcion": "   - Pulpos: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.60.00.00", "descripcion": "   - Caracoles", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.71.00.00", "descripcion": "   - Almejas vivas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.72.00.00", "descripcion": "   - Almejas congeladas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.79.00.00", "descripcion": "   - Almejas: Las demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.81.00.00", "descripcion": "   - Abulones vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.82.00.00", "descripcion": "   - Cobos vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.83.00.00", "descripcion": "   - Abulones congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.84.00.00", "descripcion": "   - Cobos congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.87.00.00", "descripcion": "   - Abulones: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.88.00.00", "descripcion": "   - Cobos: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.91.00.00", "descripcion": "   - Otros moluscos vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.92.10.00", "descripcion": "   - Locos congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.92.20.00", "descripcion": "   - Lapas congeladas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.92.90.00", "descripcion": "   - Los demás congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.99.20.00", "descripcion": "   - Locos: Otros", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.99.50.00", "descripcion": "   - Lapas: Otras", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0307.99.90.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "03.08", "descripcion": "Invertebrados acuáticos.", "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0308.11.00.00", "descripcion": "   - Pepinos de mar vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0308.12.00.00", "descripcion": "   - Pepinos de mar congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0308.19.00.00", "descripcion": "   - Pepinos de mar: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0308.21.00.00", "descripcion": "   - Erizos de mar vivos", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0308.22.00.00", "descripcion": "   - Erizos de mar congelados", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0308.29.00.00", "descripcion": "   - Erizos de mar: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0308.30.00.00", "descripcion": "   - Medusas", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0308.90.00.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "03.09", "descripcion": "Harina, polvo y pellets.", "gravamen": None,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0309.10.00.00", "descripcion": "   - De pescado", "gravamen": 10,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0309.90.10.10", "descripcion": "   - De crustáceos: Congelados", "gravamen": 15,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0309.90.10.90", "descripcion": "   - De crustáceos: Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        },
        {
            "codigo": "0309.90.90.00", "descripcion": "   - Los demás", "gravamen": 20,
            "ice_iehd": None, "unidad_medida": "kg", "despacho_frontera": None, "tipo_doc": "C'", "entidad_emite": "MORyT (SENASAG)", "disp_legal": "Ley 830 - Dec. 515", "pref_can_ace": 100, "pref_ace22_chi": None, "pref_ace22_prot": None, "pref_ace66_mexico": 100
        }
        ]

        # ... (aquí arriba está tu lista_datos gigante que NO debes tocar) ...

        self.stdout.write("Iniciando carga de datos en Aduanatech...")

        contador = 0
        total = len(datos)
        
        for item in datos:
            try:
                obj, created = Arancel.objects.update_or_create(
                    codigo=item['codigo'],
                    defaults={
                        'descripcion': item['descripcion'],
                        'gravamen': item['gravamen'],
                        
                        # Usamos .get() para que si el campo no existe en la lista, ponga None
                        'ice_iehd': item.get('ice_iehd'),
                        'unidad_medida': item.get('unidad_medida'),
                        'despacho_frontera': item.get('despacho_frontera'),
                        'tipo_doc': item.get('tipo_doc'),
                        'entidad_emite': item.get('entidad_emite'),
                        'disp_legal': item.get('disp_legal'),
                        'pref_can_ace': item.get('pref_can_ace'),
                        'pref_ace22_chi': item.get('pref_ace22_chi'),
                        'pref_ace22_prot': item.get('pref_ace22_prot'),
                        'pref_ace66_mexico': item.get('pref_ace66_mexico'),
                        'nota_explicativa': item.get('nota_explicativa'),
                        
                        # --- AQUÍ ESTÁ EL CAMPO NUEVO ---
                        # Al usar .get(), no necesitas agregarlo a los cientos de items de arriba.
                        # Solo lo tomará si decides agregárselo a uno específico.
                        'nota_explicativa': item.get('nota_explicativa'), 
                    }
                )
                if created:
                    contador += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error en código {item.get('codigo', 'DESCONOCIDO')}: {e}"))

        self.stdout.write(self.style.SUCCESS(f'¡Proceso finalizado! Se gestionaron {total} registros.'))