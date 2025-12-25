---
marp: true
theme: default
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&display=swap');
  
  :root {
    font-family: Outfit, Helvetica, Arial;
  }
  
  section {
    background-color: #ffffff;
    background-image: linear-gradient(to bottom right, #cadaf7 5%, #87a7e4 95%);
  }
  
  h1, h2, h3, h4, h5, h6 {
    color: #214484;
    font-weight: 700;
  }
  
  a {
    color: #303ca6;
  }
  
  code {
    background-color: #ffffffad;
  }
  
  mark {
    background-color: #eaa2ee;
    padding: 0 2px 2px;
  }
  
  pre {
    background-color: #ffffffad;
  }
  
  section::after {
    font-size: 0.75em;
    content: attr(data-marpit-pagination) " / " attr(data-marpit-pagination-total);
    color: #303ca6;
  }
  
  img[alt~="center"] {
    display: block;
    margin: 0 auto;
  }
---

<!-- _class: lead -->
# ISC-ITCM
## Sitio Web Oficial del Programa

**Ingeniería en Sistemas Computacionales**
Instituto Tecnológico de Ciudad Madero

**Jesús Olvera**
© 2025

---

## 📋 Descripción General

Sitio web moderno y responsive para el programa de Ingeniería en Sistemas Computacionales del ITCM.

**Objetivos:**
- ✅ Informar sobre el programa académico
- ✅ Mostrar plan de estudios y especialidades
- ✅ Presentar instalaciones y docentes
- ✅ Facilitar contacto con aspirantes

**URL:** [https://jjho05.github.io/ISC-ITCM](https://jjho05.github.io/ISC-ITCM)

---

## 🎨 Identidad Visual TecNM 2025

Diseño basado en el **Manual de Identidad Institucional TecNM 2025**

### Paleta de Colores Oficial

| Color | Código | Uso |
|-------|--------|-----|
| **Azul TecNM** | `#1B396A` | Color primario (Pantone 294 C) |
| **Gris TecNM** | `#807F83` | Texto secundario (Cool Gray 10 C) |
| **Negro** | `#000000` | Texto principal |
| **Plata** | `#ABABAB` | Detalles (Pantone 877 C) |

---

## 🏗️ Arquitectura del Sitio

```
ISC-ITCM/
├── Páginas Principales
│   ├── index.html              # Landing page
│   ├── nosotros.html          # Historia y objetivos
│   ├── plan-de-estudios.html  # Retícula completa
│   ├── perfil-aspirante.html  # Requisitos
│   ├── egresados.html         # Campo laboral
│   └── contacto.html          # Formulario
│
├── Componentes Reutilizables
│   ├── header.html            # Navegación
│   └── footer.html            # Pie de página
│
├── Semestres (1-9)
│   └── semestre[1-9]/         # Detalles por semestre
│
└── Especialidades
    ├── bigdata/               # Big Data
    └── tecweb/                # Tecnologías Web
```

---

## 🛠️ Stack Tecnológico

### Frontend
- **HTML5** - Estructura semántica
- **CSS3** - Estilos y animaciones
- **TailwindCSS** - Framework de utilidades
- **JavaScript** - Interactividad

### Tipografías Oficiales
- **Noto Sans** - Cuerpo de texto
- **Montserrat** - Títulos y encabezados

### Hosting
- **GitHub Pages** - Despliegue automático
- **CI/CD** - Actualización continua

---

## 📱 Secciones del Sitio

### 1. Inicio
- Hero section con imagen destacada
- Características del programa
- Testimonios de egresados
- Misión y visión institucional
- Call-to-action para aspirantes

### 2. Nosotros
- Historia del programa ISC-ITCM
- Objetivos educacionales
- Acreditaciones y certificaciones
- Vinculación con la industria

---

## 📱 Secciones del Sitio (continuación)

### 3. Plan de Estudios
- **Retícula completa:** 9 semestres
- **Materias por semestre** con detalles
- **Especialidades:**
  - Big Data
  - Tecnologías Web
- Mapa curricular interactivo

### 4. Perfil del Aspirante
- Requisitos de ingreso
- Habilidades deseables
- Proceso de admisión
- Fechas importantes

---

## 📱 Secciones del Sitio (continuación)

### 5. Egresados
- Perfil de egreso
- Campo laboral
- Historias de éxito
- Conferencias y eventos
- Estadísticas de empleabilidad

### 6. Contacto
- Formulario de contacto
- Información de ubicación
- Redes sociales
- Horarios de atención
- Mapa interactivo

---

## 🎯 Características Técnicas

### SEO Optimizado
```html
<!-- Meta tags para motores de búsqueda -->
<meta name="description" content="...">
<meta name="keywords" content="...">
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="...">
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

---

## 📊 Responsive Design

### Breakpoints
```css
/* Mobile First Approach */
sm: 640px   /* Móvil grande */
md: 768px   /* Tablet */
lg: 1024px  /* Desktop */
xl: 1280px  /* Desktop grande */
2xl: 1536px /* Pantallas grandes */
```

### Optimizaciones
- ✅ Imágenes responsive con `srcset`
- ✅ Lazy loading de recursos
- ✅ Menú hamburguesa en móvil
- ✅ Grid adaptativo
- ✅ Touch-friendly en móviles

---

## 📈 Rendimiento

### Métricas Lighthouse

| Métrica | Score | Objetivo |
|---------|-------|----------|
| **Performance** | 95+ | ✅ Excelente |
| **Accessibility** | 98+ | ✅ Excelente |
| **Best Practices** | 100 | ✅ Perfecto |
| **SEO** | 100 | ✅ Perfecto |

### Tiempos de Carga
- **First Contentful Paint:** < 1.5s
- **Time to Interactive:** < 3s
- **Cumulative Layout Shift:** < 0.1

---

## 🎓 Plan de Estudios

### Estructura Académica
- **Duración:** 9 semestres
- **Total de materias:** 50+
- **Horas totales:** 3,000+
- **Modalidad:** Presencial

### Especialidades (Semestres 7-9)

#### Big Data
- Minería de datos
- Análisis de datos masivos
- Machine Learning
- Visualización de datos

#### Tecnologías Web
- Desarrollo web avanzado
- Frameworks modernos
- Arquitecturas web
- Seguridad web

---

## 👥 Perfil del Aspirante

### Requisitos de Ingreso
- ✅ Certificado de bachillerato
- ✅ Acta de nacimiento
- ✅ CURP
- ✅ Fotografías tamaño infantil
- ✅ Examen de admisión CENEVAL

### Habilidades Deseables
- Pensamiento lógico-matemático
- Capacidad de análisis
- Trabajo en equipo
- Creatividad e innovación
- Interés por la tecnología

---

## 💼 Perfil de Egreso

### Competencias del Egresado

**Técnicas:**
- Desarrollo de software
- Administración de bases de datos
- Redes y telecomunicaciones
- Seguridad informática
- Gestión de proyectos

**Profesionales:**
- Liderazgo de equipos
- Comunicación efectiva
- Pensamiento crítico
- Ética profesional
- Aprendizaje continuo

---

## 🏢 Campo Laboral

### Áreas de Desempeño
- Desarrollo de software
- Administración de TI
- Consultoría tecnológica
- Seguridad informática
- Análisis de datos
- Gestión de proyectos
- Emprendimiento tecnológico

### Sectores
- Empresas privadas
- Sector público
- Instituciones educativas
- Startups tecnológicas
- Consultoría independiente

---

## 🌟 Características Destacadas

### Diseño Moderno
- ✅ Interfaz limpia y profesional
- ✅ Animaciones suaves
- ✅ Navegación intuitiva
- ✅ Accesibilidad WCAG 2.1

### Componentes Reutilizables
- ✅ Header con navegación responsive
- ✅ Footer institucional
- ✅ Cards de materias
- ✅ Testimonios
- ✅ Formularios validados

---

## 🔄 Actualizaciones Recientes

### Versión 2.0 (2025)
- ✅ Implementación identidad TecNM 2025
- ✅ Optimización de componentes
- ✅ Mejoras de rendimiento
- ✅ Cache busting
- ✅ SEO mejorado

### Mejoras de UX
- ✅ Navegación más intuitiva
- ✅ Tiempos de carga reducidos
- ✅ Mejor accesibilidad
- ✅ Formularios optimizados

---

## 📞 Información de Contacto

### Instituto Tecnológico de Ciudad Madero
**Tecnológico Nacional de México**

- 🌐 **Web:** [www.cdmadero.tecnm.mx](https://www.cdmadero.tecnm.mx/)
- 📧 **Email:** sistemas@cdmadero.tecnm.mx
- 📍 **Ubicación:** Cd. Madero, Tamaulipas, México
- 📱 **Teléfono:** (833) 357 5940

### Coordinación ISC
- 📧 **Email:** coordinacion.isc@cdmadero.tecnm.mx
- 🕐 **Horario:** Lunes a Viernes, 8:00 - 18:00

---

## 🚀 Instalación y Desarrollo

### Clonar Repositorio
```bash
git clone https://github.com/jjho05/ISC-ITCM.git
cd ISC-ITCM
```

### Servidor Local
```bash
# Con Python
python3 -m http.server 8000

# Con Node.js
npx http-server

# Abrir en http://localhost:8000
```

### Live Server (VS Code)
1. Instalar extensión "Live Server"
2. Click derecho en `index.html`
3. "Open with Live Server"

---

## 🤝 Contribuciones

### Guías de Estilo
- Seguir identidad visual TecNM
- Usar componentes reutilizables
- Mantener código semántico
- Optimizar imágenes (WebP)
- Probar en múltiples dispositivos

### Proceso de Contribución
1. Fork del proyecto
2. Crear rama (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -m 'feat: añadir mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abrir Pull Request

---

## 📄 Licencia y Créditos

### Licencia
Este proyecto es propiedad del **Instituto Tecnológico de Ciudad Madero** (TecNM).

### Desarrollo
**Jesús Olvera**
- GitHub: [@jjho05](https://github.com/jjho05)
- Email: jjho.reivaj05@gmail.com

### Agradecimientos
- TecNM por las guías de identidad visual
- Comunidad ISC-ITCM
- Profesores y coordinadores
- Egresados que compartieron testimonios

---

<!-- _class: lead -->
# ¡Gracias!

**ISC-ITCM - Formando Profesionales de Excelencia**

🌐 [jjho05.github.io/ISC-ITCM](https://jjho05.github.io/ISC-ITCM)
📧 sistemas@cdmadero.tecnm.mx

**Instituto Tecnológico de Ciudad Madero**
Tecnológico Nacional de México

---
