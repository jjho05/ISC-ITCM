#!/usr/bin/env python3
"""
Script para actualizar todas las páginas HTML con los colores y tipografía oficial del TecNM
Actualiza: colores oficiales (Pantone 294 C) y tipografías (Noto Sans + Montserrat)
"""

import os
import re
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).parent

# Colores antiguos y nuevos
OLD_COLORS = {
    '--primary-color: #1978e5': '--primary-color: #1B396A',
    '--text-primary: #111418': '--text-primary: #000000',
    '--text-secondary: #637488': '--text-secondary: #807F83',
}

# Tipografías antiguas y nuevas
OLD_FONT = 'Work+Sans'
NEW_FONTS = [
    'Noto+Sans',
    'Montserrat'
]

def update_html_file(filepath):
    """Actualiza un archivo HTML con los nuevos colores y tipografías del TecNM"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        changes_made = []
        
        # 1. Actualizar enlace de Google Fonts
        if 'Work+Sans' in content:
            # Reemplazar Work Sans con Noto Sans y Montserrat
            old_font_link = re.search(
                r'<link[^>]*href="https://fonts\.googleapis\.com/css2\?family=Work\+Sans[^"]*"[^>]*>',
                content
            )
            
            if old_font_link:
                new_fonts_html = '''<!-- Tipografías Oficiales TecNM -->
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap" rel="stylesheet" />'''
                
                content = content.replace(old_font_link.group(0), new_fonts_html)
                changes_made.append('Tipografías actualizadas')
        
        # 2. Actualizar variables CSS en <style>
        style_block = re.search(
            r'<style[^>]*>.*?:root\s*{(.*?)}\s*body\s*{(.*?)}\s*</style>',
            content,
            re.DOTALL
        )
        
        if style_block:
            old_style = style_block.group(0)
            new_style = old_style
            
            # Actualizar colores
            for old_color, new_color in OLD_COLORS.items():
                if old_color in new_style:
                    new_style = new_style.replace(old_color, new_color)
                    changes_made.append(f'Color actualizado: {old_color.split(":")[0]}')
            
            # Actualizar tipografía del body
            new_style = new_style.replace(
                'font-family: "Work Sans", sans-serif;',
                'font-family: "Noto Sans", sans-serif;'
            )
            
            # Agregar estilos para títulos si no existen
            if 'h1, h2, h3, h4, h5, h6' not in new_style:
                # Insertar antes del cierre de </style>
                heading_styles = '''
        h1, h2, h3, h4, h5, h6 {
            font-family: "Montserrat", sans-serif;
            font-weight: 700;
        }
    '''
                new_style = new_style.replace('</style>', heading_styles + '</style>')
                changes_made.append('Estilos de títulos agregados')
            
            content = content.replace(old_style, new_style)
        
        # 3. Actualizar colores inline si existen (en algunos archivos)
        content = re.sub(
            r'#1978e5',
            '#1B396A',
            content
        )
        
        # Solo guardar si hubo cambios
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, changes_made
        else:
            return False, []
            
    except Exception as e:
        print(f"❌ Error procesando {filepath}: {e}")
        return False, []

def main():
    """Función principal"""
    print("🎨 Actualizando sitio ISC-ITCM con identidad oficial TecNM")
    print("=" * 60)
    
    # Contadores
    total_files = 0
    updated_files = 0
    skipped_files = 0
    
    # Archivos a actualizar
    html_files = []
    
    # Páginas principales
    for file in BASE_DIR.glob('*.html'):
        if file.name not in ['update_pages.py']:
            html_files.append(file)
    
    # Páginas de semestres
    for i in range(1, 10):
        semester_dir = BASE_DIR / f'semestre{i}'
        if semester_dir.exists():
            html_files.extend(semester_dir.glob('*.html'))
    
    # Páginas de especialidades
    for specialty in ['bigdata', 'tecweb']:
        specialty_dir = BASE_DIR / specialty
        if specialty_dir.exists():
            html_files.extend(specialty_dir.glob('*.html'))
    
    total_files = len(html_files)
    print(f"\n📄 Archivos HTML encontrados: {total_files}")
    print("-" * 60)
    
    # Procesar cada archivo
    for filepath in html_files:
        relative_path = filepath.relative_to(BASE_DIR)
        updated, changes = update_html_file(filepath)
        
        if updated:
            updated_files += 1
            print(f"✅ {relative_path}")
            for change in changes:
                print(f"   → {change}")
        else:
            skipped_files += 1
            print(f"⏭️  {relative_path} (sin cambios)")
    
    # Resumen final
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE ACTUALIZACIÓN")
    print("=" * 60)
    print(f"Total de archivos: {total_files}")
    print(f"✅ Actualizados: {updated_files}")
    print(f"⏭️  Sin cambios: {skipped_files}")
    print("\n🎉 Actualización completada!")
    print("\n📝 Cambios aplicados:")
    print("   • Color primario: #1978e5 → #1B396A (Pantone 294 C)")
    print("   • Tipografía cuerpo: Work Sans → Noto Sans")
    print("   • Tipografía títulos: Work Sans → Montserrat")
    print("   • Colores de texto: Ajustados a paleta oficial")

if __name__ == '__main__':
    main()
