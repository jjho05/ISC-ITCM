#!/usr/bin/env python3
"""
Script mejorado para actualizar todas las páginas HTML del sitio ISC-ITCM
para usar el sistema de componentes (header y footer)
"""

import os
import re
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path("/Users/lic.ing.jesusolvera/Documents/PROYECTOS PERSONALES/ISC-ITCM")

# Páginas principales en la raíz
MAIN_PAGES = [
    "nosotros.html",
    "plan-de-estudios.html",
    "contacto.html",
    "perfil-aspirante.html",
    "egresados.html",
    "gracias.html"
]

def update_html_file(filepath, is_subdirectory=False):
    """
    Actualiza un archivo HTML para usar componentes
    
    Args:
        filepath: Ruta al archivo HTML
        is_subdirectory: True si el archivo está en un subdirectorio
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Determinar rutas relativas según la ubicación
        if is_subdirectory:
            css_path = "../css/styles.css"
            js_loader_path = "../js/components-loader.js"
            js_menu_path = "../js/menu.js"
        else:
            css_path = "css/styles.css"
            js_loader_path = "js/components-loader.js"
            js_menu_path = "js/menu.js"
        
        # 1. Agregar link al CSS global si no existe
        if 'css/styles.css' not in content and '../css/styles.css' not in content:
            # Buscar la línea de Work Sans font
            if 'Work+Sans' in content:
                content = content.replace(
                    '<link href="https://fonts.googleapis.com/css2?family=Work+Sans',
                    f'<link href="{css_path}" rel="stylesheet"/>\n    <link href="https://fonts.googleapis.com/css2?family=Work+Sans'
                )
        
        # 2. Reemplazar header con placeholder - Patrón más robusto
        # Buscar desde <header hasta el cierre de mobile-menu
        header_patterns = [
            # Patrón 1: Con comentario "PEGAR EN"
            r'<!-- PEGAR EN:.*?-->\s*<header.*?</header>\s*<div id="mobile-menu".*?</div>',
            # Patrón 2: Con comentario "HEADER"
            r'<!-- HEADER.*?-->\s*<header.*?</header>\s*<div id="mobile-menu".*?</div>',
            # Patrón 3: Solo header sin comentario
            r'<header\s+class="sticky top-0.*?</header>\s*<div id="mobile-menu".*?</div>',
        ]
        
        header_replaced = False
        for pattern in header_patterns:
            if re.search(pattern, content, flags=re.DOTALL):
                content = re.sub(
                    pattern,
                    '        <!-- Header Component -->\n        <div id="header-placeholder"></div>',
                    content,
                    flags=re.DOTALL
                )
                header_replaced = True
                break
        
        # 3. Reemplazar footer con placeholder - Patrón más robusto
        footer_patterns = [
            # Patrón 1: Con comentario "FOOTER"
            r'<!-- FOOTER.*?-->\s*<footer.*?</footer>',
            # Patrón 2: Footer con clase bg-[var(--secondary-color)]
            r'<footer\s+class="bg-\[var\(--secondary-color\)\].*?</footer>',
        ]
        
        footer_replaced = False
        for pattern in footer_patterns:
            if re.search(pattern, content, flags=re.DOTALL):
                content = re.sub(
                    pattern,
                    '\n        <!-- Footer Component -->\n        <div id="footer-placeholder"></div>',
                    content,
                    flags=re.DOTALL
                )
                footer_replaced = True
                break
        
        # 4. Eliminar script del menú móvil si existe
        menu_script_patterns = [
            r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\'.*?}\);\s*</script>',
            r'<script>\s*document\.addEventListener\("DOMContentLoaded".*?}\);\s*</script>',
        ]
        
        for pattern in menu_script_patterns:
            content = re.sub(pattern, '', content, flags=re.DOTALL)
        
        # 5. Agregar scripts de componentes antes de </body> si no existen
        if 'components-loader.js' not in content:
            # Buscar </body> y agregar scripts antes
            if '</body>' in content:
                scripts = f'\n<!-- Component Loader Scripts -->\n<script src="{js_loader_path}"></script>\n<script src="{js_menu_path}"></script>\n</body>'
                content = content.replace('</body>', scripts)
        
        # Solo guardar si hubo cambios
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            status = "✅"
            if header_replaced and footer_replaced:
                status += " (Header + Footer)"
            elif header_replaced:
                status += " (Solo Header)"
            elif footer_replaced:
                status += " (Solo Footer)"
            else:
                status += " (Scripts/CSS)"
            
            print(f"{status} Actualizado: {filepath.name}")
            return True
        else:
            print(f"⏭️  Sin cambios: {filepath.name}")
            return False
        
    except Exception as e:
        print(f"❌ Error en {filepath.name}: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Iniciando actualización de páginas HTML (v2)...")
    print(f"📁 Directorio base: {BASE_DIR}\n")
    
    updated_count = 0
    skipped_count = 0
    failed_count = 0
    
    # Actualizar páginas principales
    print("📄 Actualizando páginas principales...")
    for page in MAIN_PAGES:
        filepath = BASE_DIR / page
        if filepath.exists():
            result = update_html_file(filepath, is_subdirectory=False)
            if result:
                updated_count += 1
            elif result is False:
                failed_count += 1
            else:
                skipped_count += 1
        else:
            print(f"⚠️  No encontrado: {page}")
    
    # Actualizar páginas de semestres
    print("\n📚 Actualizando páginas de semestres...")
    for i in range(1, 10):
        semester_dir = BASE_DIR / f"semestre{i}"
        if semester_dir.exists() and semester_dir.is_dir():
            html_files = list(semester_dir.glob("*.html"))
            for html_file in html_files:
                result = update_html_file(html_file, is_subdirectory=True)
                if result:
                    updated_count += 1
                elif result is False:
                    failed_count += 1
                else:
                    skipped_count += 1
    
    # Actualizar páginas de especialidades
    print("\n🎓 Actualizando páginas de especialidades...")
    for specialty in ["bigdata", "tecweb"]:
        specialty_dir = BASE_DIR / specialty
        if specialty_dir.exists() and specialty_dir.is_dir():
            html_files = list(specialty_dir.glob("*.html"))
            for html_file in html_files:
                result = update_html_file(html_file, is_subdirectory=True)
                if result:
                    updated_count += 1
                elif result is False:
                    failed_count += 1
                else:
                    skipped_count += 1
    
    # Actualizar otras carpetas
    print("\n📂 Actualizando otras carpetas...")
    for folder in ["docentes", "instalaciones", "conferenciasegresados"]:
        folder_dir = BASE_DIR / folder
        if folder_dir.exists() and folder_dir.is_dir():
            html_files = list(folder_dir.glob("*.html"))
            for html_file in html_files:
                result = update_html_file(html_file, is_subdirectory=True)
                if result:
                    updated_count += 1
                elif result is False:
                    failed_count += 1
                else:
                    skipped_count += 1
    
    # Resumen
    print("\n" + "="*50)
    print(f"✅ Archivos actualizados exitosamente: {updated_count}")
    print(f"⏭️  Archivos sin cambios: {skipped_count}")
    print(f"❌ Archivos con errores: {failed_count}")
    print(f"📊 Total procesados: {updated_count + skipped_count + failed_count}")
    print("="*50)
    print("\n✨ ¡Actualización completada!")

if __name__ == "__main__":
    main()
