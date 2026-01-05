# 🎓 ISC-ITCM - Sitio Web Oficial

> Página web oficial del programa de Ingeniería en Sistemas Computacionales del Instituto Tecnológico de Ciudad Madero (TecNM)

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://www.w3.org/Style/CSS/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind-38B2AC?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## 🌐 Demo

**Sitio en Vivo:** [https://jjho05.github.io/ISC-ITCM](https://jjho05.github.io/ISC-ITCM)

## 📋 Descripción

Sitio web moderno y responsive para el programa de Ingeniería en Sistemas Computacionales del ITCM, diseñado siguiendo la identidad visual oficial del TecNM 2025.

### Características Principales

- ✅ **Diseño Responsive** - Optimizado para todos los dispositivos
- ✅ **Identidad TecNM** - Colores y tipografías oficiales
- ✅ **SEO Optimizado** - Meta tags y estructura semántica
- ✅ **Componentes Reutilizables** - Header y Footer modulares
- ✅ **Navegación Intuitiva** - Menú hamburguesa en móvil
- ✅ **Rendimiento Optimizado** - Carga rápida y eficiente

## 🎨 Paleta de Colores Oficial TecNM

```css
--tecnm-blue: #1B396A;      /* Pantone 294 C - Azul oficial */
--tecnm-gray: #807F83;      /* Cool Gray 10 C */
--tecnm-black: #000000;     /* Negro 100% */
--tecnm-silver: #ABABAB;    /* Pantone 877 C */
```

## 📁 Estructura del Proyecto

```
ISC-ITCM/
├── index.html                  # Página principal
├── nosotros.html              # Acerca del programa
├── plan-de-estudios.html      # Plan de estudios
├── perfil-aspirante.html      # Perfil del aspirante
├── egresados.html             # Egresados destacados
├── contacto.html              # Formulario de contacto
├── gracias.html               # Página de confirmación
│
├── components/                # Componentes reutilizables
│   ├── header.html           # Header con navegación
│   └── footer.html           # Footer institucional
│
├── css/
│   └── styles.css            # Estilos personalizados
│
├── js/
│   ├── components-loader.js  # Cargador de componentes
│   └── menu.js               # Lógica del menú móvil
│
├── semestre1-9/              # Páginas de semestres
│   └── *.html                # Detalles por semestre
│
├── bigdata/                  # Especialidad Big Data
├── tecweb/                   # Especialidad Tecnologías Web
├── instalaciones/            # Galería de instalaciones
└── docentes/                 # Perfiles de profesores
```

## 🚀 Instalación y Uso

### Opción 1: Clonar y Abrir Localmente

```bash
# Clonar repositorio
git clone https://github.com/jjho05/ISC-ITCM.git
cd ISC-ITCM

# Abrir en navegador
open index.html
```

### Opción 2: Servidor Local

```bash
# Con Python
python3 -m http.server 8000

# Con Node.js (http-server)
npx http-server

# Abrir navegador en http://localhost:8000
```

### Opción 3: Live Server (VS Code)

1. Instalar extensión "Live Server"
2. Click derecho en `index.html`
3. Seleccionar "Open with Live Server"

## 🛠️ Tecnologías Utilizadas

- **HTML5** - Estructura semántica
- **CSS3** - Estilos y animaciones
- **TailwindCSS** - Framework de utilidades CSS
- **JavaScript** - Interactividad y componentes
- **Google Fonts** - Tipografías oficiales TecNM
  - Noto Sans (cuerpo)
  - Montserrat (títulos)

## 📱 Secciones del Sitio

### 1. Inicio (`index.html`)
- Hero section con imagen destacada
- Características del programa
- Testimonios de egresados
- Misión y visión
- Call-to-action

### 2. Nosotros (`nosotros.html`)
- Historia del programa
- Objetivos educacionales
- Acreditaciones
- Vinculación con la industria

### 3. Plan de Estudios (`plan-de-estudios.html`)
- Retícula completa (9 semestres)
- Especialidades:
  - Big Data
  - Tecnologías Web
- Materias por semestre

### 4. Perfil del Aspirante (`perfil-aspirante.html`)
- Requisitos de ingreso
- Habilidades deseables
- Proceso de admisión

### 5. Egresados (`egresados.html`)
- Perfil de egreso
- Campo laboral
- Historias de éxito
- Conferencias

### 6. Contacto (`contacto.html`)
- Formulario de contacto
- Información de ubicación
- Redes sociales
- Horarios de atención

## 🎯 Características Técnicas

### SEO

```html
<!-- Meta tags optimizados -->
<meta name="description" content="...">
<meta name="keywords" content="...">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
```

### Componentes Modulares

```javascript
// Carga dinámica de header y footer
fetch('components/header.html')
  .then(response => response.text())
  .then(data => {
    document.getElementById('header-placeholder').innerHTML = data;
  });
```

### Responsive Design

```css
/* Breakpoints */
sm: 640px   /* Móvil grande */
md: 768px   /* Tablet */
lg: 1024px  /* Desktop */
xl: 1280px  /* Desktop grande */
```

## 📊 Rendimiento

- ✅ **Lighthouse Score:** 95+
- ✅ **First Contentful Paint:** < 1.5s
- ✅ **Time to Interactive:** < 3s
- ✅ **Cumulative Layout Shift:** < 0.1

## 🔄 Actualizaciones Recientes

- ✅ Implementación identidad oficial TecNM 2025
- ✅ Optimización de layout y componentes
- ✅ Corrección de typos y mejoras de UX
- ✅ Cache busting para actualizaciones inmediatas
- ✅ Ajustes de alineación en footer

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -m 'feat: añadir mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

### Guías de Estilo

- Seguir identidad visual TecNM
- Usar componentes reutilizables
- Mantener código semántico
- Optimizar imágenes
- Probar en múltiples dispositivos

## 📄 Licencia

Este proyecto es propiedad del Instituto Tecnológico de Ciudad Madero (TecNM).

## 👥 Autores

- **Jesús Olvera** - *Desarrollo y diseño* - [@jjho05](https://github.com/jjho05)

## 🏫 Institución

**Instituto Tecnológico de Ciudad Madero**  
Tecnológico Nacional de México

- 🌐 [Sitio Oficial ITCM](https://www.cdmadero.tecnm.mx/)
- 📧 Email: sistemas@cdmadero.tecnm.mx
- 📍 Cd. Madero, Tamaulipas, México

## 🙏 Agradecimientos

- TecNM por las guías de identidad visual
- Comunidad ISC-ITCM
- Profesores y coordinadores del programa
- Egresados que compartieron sus testimonios

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub

**Hecho con ❤️ para el ISC-ITCM**
