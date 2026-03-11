import { defineConfig } from 'vite';
import { resolve } from 'path';
import { viteStaticCopy } from 'vite-plugin-static-copy';

export default defineConfig({
  base: '/ISC-ITCM/',
  plugins: [
    viteStaticCopy({
      targets: [
        {
          src: 'components',
          dest: ''
        }
      ]
    })
  ],
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        contacto: resolve(__dirname, 'contacto.html'),
        egresados: resolve(__dirname, 'egresados.html'),
        gracias: resolve(__dirname, 'gracias.html'),
        nosotros: resolve(__dirname, 'nosotros.html'),
        perfil: resolve(__dirname, 'perfil-aspirante.html'),
        plan: resolve(__dirname, 'plan-de-estudios.html'),
      },
    },
  },
});
