/**
 * Components Loader
 * Carga header y footer dinámicamente y maneja navegación activa
 */

(function () {
    'use strict';

    // Obtener el BASE_URL de Vite (ej: '/ISC-ITCM/' o '/')
    const BASE_URL = import.meta.env.BASE_URL || '/';

    // Detectar profundidad de la carpeta actual
    function getRelativeDepth() {
        const path = window.location.pathname;
        const base = BASE_URL.endsWith('/') ? BASE_URL : BASE_URL + '/';
        
        // Si estamos en la raíz (ej: /ISC-ITCM/ o /ISC-ITCM/index.html)
        let relativePath = path;
        if (path.startsWith(base)) {
            relativePath = path.substring(base.length);
        }
        
        // Contar cuántas carpetas hay
        const folders = relativePath.split('/').filter(p => p.length > 0 && !p.endsWith('.html'));
        return folders.length;
    }

    // Cargar un componente
    async function loadComponent(componentName, placeholderId) {
        const componentPath = `${BASE_URL}components/${componentName}.html`.replace(/\/+/g, '/');

        try {
            const response = await fetch(componentPath);
            if (!response.ok) throw new Error(`Error loading ${componentName}: ${response.status}`);
            const html = await response.text();
            const placeholder = document.getElementById(placeholderId);
            if (placeholder) placeholder.innerHTML = html;
        } catch (error) {
            console.error(`Failed to load ${componentName}:`, error);
        }
    }

    // Detectar página actual y marcar navegación activa
    function setActiveNavigation() {
        const pathParts = window.location.pathname.split('/');
        const currentPage = pathParts[pathParts.length - 1].replace('.html', '') || 'index';

        const navLinks = document.querySelectorAll('header nav a[data-page], #mobile-menu a[data-page-mobile]');
        navLinks.forEach(link => {
            const linkPage = link.getAttribute('data-page') || link.getAttribute('data-page-mobile');
            if (linkPage === currentPage) {
                link.classList.remove('text-[var(--text-secondary)]', 'font-medium');
                link.classList.add('text-[var(--primary-color)]', 'font-bold');
            }
        });
    }

    // Ajustar rutas relativas en los componentes según la profundidad
    function adjustComponentPaths() {
        const depth = getRelativeDepth();
        if (depth === 0) return;

        const prefix = '../'.repeat(depth);
        const elements = document.querySelectorAll('header a[href], footer a[href], #mobile-menu a[href], header img[src], footer img[src]');
        
        elements.forEach(el => {
            const attr = el.tagName === 'A' ? 'href' : 'src';
            const val = el.getAttribute(attr);
            
            if (val && !val.startsWith('http') && !val.startsWith('#') && !val.startsWith('/') && !val.startsWith('../')) {
                el.setAttribute(attr, prefix + val);
            }
        });
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
