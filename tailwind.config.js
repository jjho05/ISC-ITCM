/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./contacto.html",
    "./egresados.html",
    "./gracias.html",
    "./nosotros.html",
    "./perfil-aspirante.html",
    "./plan-de-estudios.html",
    "./components/**/*.html",
    "./js/**/*.js",
    "./**/*.html"
  ],
  theme: {
    extend: {
      colors: {
        tecnm: {
          blue: '#1B396A',
          gray: '#807F83',
          black: '#000000',
          silver: '#ABABAB',
        }
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries'),
  ],
}
