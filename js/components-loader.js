/**
 * Components Loader
 * Carga header y footer dinámicamente y maneja navegación activa
 */

(function () {
    'use strict';

    // Obtener el BASE_URL de Vite (ej: '/ISC-ITCM/' o '/')
    const BASE_URL = import.meta.env.BASE_URL || '/';

    // Detectar profundidad de la carpeta actual para otros ajustes si son necesarios
    function getRelativeDepth() {
        const path = window.location.pathname;
        const base = BASE_URL.endsWith('/') ? BASE_URL : BASE_URL + '/';
        
        let relativePath = path;
        if (path.startsWith(base)) {
            relativePath = path.substring(base.length - 1);
        }
        return (relativePath.match(/\//g) || []).length - 1;
    }

    // Cargar un componente
    async function loadComponent(componentName, placeholderId) {
        // Usamos BASE_URL para asegurar que la ruta sea siempre absoluta respecto al repo
        const componentPath = `${BASE_URL}components/${componentName}.html`.replace(/\/+/g, '/');

        try {
            const response = await fetch(componentPath);
            if (!response.ok) {
                throw new Error(`Error loading ${componentName}: ${response.status}`);
            }
            const html = await response.text();
            const placeholder = document.getElementById(placeholderId);
            if (placeholder) {
                placeholder.innerHTML = html;
            }
        } catch (error) {
            console.error(`Failed to load ${componentName}:`, error);
        }
    }

    // Detectar página actual y marcar navegación activa
    function setActiveNavigation() {
        const currentPage = window.location.pathname.split('/').pop().replace('.html', '') || 'index';

        // Navegación desktop
        const navLinks = document.querySelectorAll('header nav a[data-page]');
        navLinks.forEach(link => {
            const linkPage = link.getAttribute('data-page');
            if (linkPage === currentPage) {
                link.classList.remove('text-[var(--text-secondary)]', 'font-medium');
                link.classList.add('text-[var(--primary-color)]', 'font-bold');
            }
        });

        // Navegación móvil
        const mobileLinks = document.querySelectorAll('#mobile-menu a[data-page-mobile]');
        mobileLinks.forEach(link => {
            const linkPage = link.getAttribute('data-page-mobile');
            if (linkPage === currentPage) {
                link.classList.remove('text-[var(--text-secondary)]');
                link.classList.add('text-[var(--primary-color)]');
            }
        });
    }

    // Ajustar rutas relativas en los componentes según la profundidad (para imágenes o links internos)
    function adjustComponentPaths() {
        const depth = getRelativeDepth();

        // Solo ajustar si estamos en un subdirectorio
        if (depth > 1) {
            const links = document.querySelectorAll('header a[href], footer a[href], #mobile-menu a[href]');
            links.forEach(link => {
                const href = link.getAttribute('href');
                if (href && !href.startsWith('http') && !href.startsWith('#') && !href.startsWith('../')) {
                    link.setAttribute('href', '../' + href);
                }
            });

            const images = document.querySelectorAll('header img[src], footer img[src]');
            images.forEach(img => {
                const src = img.getAttribute('src');
                if (src && !src.startsWith('http') && !src.startsWith('../')) {
                    img.setAttribute('src', '../' + src);
                }
            });
        }
    }

    // Inicializar cuando el DOM esté listo
    async function init() {
        await Promise.all([
            loadComponent('header', 'header-placeholder'),
            loadComponent('footer', 'footer-placeholder')
        ]);

        adjustComponentPaths();
        setActiveNavigation();
        document.dispatchEvent(new Event('componentsLoaded'));
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
