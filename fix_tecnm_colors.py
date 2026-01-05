#!/usr/bin/env python3
"""
Script para corregir el color secundario no oficial en todos los archivos HTML
Cambia --secondary-color: #0d3b66 por --secondary-color: #14305C
para cumplir con el manual de identidad TecNM
"""

import os
import re
from pathlib import Path

def fix_secondary_color(file_path):
    """Corrige el color secundario en un archivo HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar y reemplazar el color no oficial
        original_color = '--secondary-color: #0d3b66;'
        new_color = '--secondary-color: #14305C;'
        
        if original_color in content:
            new_content = content.replace(original_color, new_color)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            return True
        
        return False
    
    except Exception as e:
        print(f"❌ Error en {file_path}: {e}")
        return False

def main():
    """Función principal"""
    base_dir = Path(__file__).parent
    
    # Buscar todos los archivos HTML
    html_files = list(base_dir.rglob('*.html'))
    
    print(f"🔍 Encontrados {len(html_files)} archivos HTML")
    print("🔧 Corrigiendo color secundario no oficial TecNM...\n")
    
    fixed_count = 0
    skipped_count = 0
    
    for html_file in html_files:
        if fix_secondary_color(html_file):
            print(f"✅ Corregido: {html_file.relative_to(base_dir)}")
            fixed_count += 1
        else:
            skipped_count += 1
    
    print(f"\n{'='*60}")
    print(f"📊 RESUMEN:")
    print(f"   ✅ Archivos corregidos: {fixed_count}")
    print(f"   ⏭️  Archivos sin cambios: {skipped_count}")
    print(f"   📁 Total procesados: {len(html_files)}")
    print(f"{'='*60}")
    
    if fixed_count > 0:
        print("\n✨ Corrección completada exitosamente")
        print("🎨 Todos los archivos ahora cumplen con el manual de identidad TecNM")
    else:
        print("\n✅ Todos los archivos ya estaban correctos")

if __name__ == '__main__':
    main()
