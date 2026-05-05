import os
import re
from pathlib import Path

BASE_DIR = Path("/Users/lic.ing.jesusolvera/Documents/PROYECTOS PERSONALES/ISC-ITCM")

def fix_script_tags(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Asegurar que components-loader.js sea type="module"
        content = re.sub(
            r'<script\s+(?:type="[^"]*"\s+)?src="([^"]*components-loader\.js)"',
            r'<script type="module" src="\1"',
            content
        )
        
        # 2. Asegurar que menu.js sea type="module" (opcional pero recomendado si usa imports)
        content = re.sub(
            r'<script\s+(?:type="[^"]*"\s+)?src="([^"]*menu\.js)"',
            r'<script type="module" src="\1"',
            content
        )

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed scripts in: {filepath.relative_to(BASE_DIR)}")
            return True
        return False
    except Exception as e:
        print(f"❌ Error in {filepath}: {e}")
        return False

def main():
    print("Fixing script tags to use type='module'...")
    for root, dirs, files in os.walk(BASE_DIR):
        if 'node_modules' in dirs: dirs.remove('node_modules')
        if 'dist' in dirs: dirs.remove('dist')
        if '.git' in dirs: dirs.remove('.git')
        
        for file in files:
            if file.endswith('.html'):
                fix_script_tags(Path(root) / file)

if __name__ == "__main__":
    main()
