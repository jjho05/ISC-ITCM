import { defineConfig } from 'vite';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';
import { viteStaticCopy } from 'vite-plugin-static-copy';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Función para obtener todos los archivos HTML recursivamente
function getHtmlEntries(dir, entries = {}) {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const filePath = resolve(dir, file);
    const stats = fs.statSync(filePath);
    
    // Ignorar carpetas irrelevantes
    if (stats.isDirectory()) {
      if (!['node_modules', 'dist', '.git', 'components', 'public', 'assets'].includes(file)) {
        getHtmlEntries(filePath, entries);
      }
    } else if (file.endsWith('.html')) {
      const relativePath = filePath.replace(__dirname, '').replace(/\\/g, '/').replace(/^\//, '');
      const name = relativePath.replace(/\.html$/, '').replace(/\//g, '_') || 'index';
      entries[name] = filePath;
    }
  });
  return entries;
}

export default defineConfig({
  base: '/ISC-ITCM/',
  plugins: [
    viteStaticCopy({
      targets: [
        {
          src: 'components',
          dest: ''
        },
        {
            src: 'assets',
            dest: ''
        }
      ]
    })
  ],
  build: {
    rollupOptions: {
      input: getHtmlEntries(__dirname),
    },
    outDir: 'dist',
    emptyOutDir: true,
  },
  server: {
    open: true,
  }
});
