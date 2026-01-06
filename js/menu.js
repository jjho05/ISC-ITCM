/**
 * Menu Handler - ISC-ITCM
 * Maneja la funcionalidad del menú móvil con transición
 */

(function () {
    'use strict';

    function initMenu() {
        const menuBtn = document.getElementById('menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        const menuIconOpen = document.getElementById('menu-icon-open');
        const menuIconClose = document.getElementById('menu-icon-close');

        if (!menuBtn || !mobileMenu || !menuIconOpen || !menuIconClose) {
            console.warn('Menu elements not found. Waiting for components to load...');
            return;
        }

        // Toggle del menú con transición
        const toggleMenu = () => {
            const isHidden = mobileMenu.classList.contains('hidden');

            if (isHidden) {
                // Abrir menú con transición
                mobileMenu.classList.remove('hidden');
                // Forzar reflow
                mobileMenu.offsetHeight;
                mobileMenu.classList.remove('translate-x-full');

                menuIconOpen.classList.toggle('hidden');
                menuIconClose.classList.toggle('hidden');
                document.body.style.overflow = 'hidden';
            } else {
                // Cerrar menú con transición
                mobileMenu.classList.add('translate-x-full');

                setTimeout(() => {
                    mobileMenu.classList.add('hidden');
                }, 300);

                menuIconOpen.classList.toggle('hidden');
                menuIconClose.classList.toggle('hidden');
                document.body.style.overflow = '';
            }
        };

        // Click en el botón del menú
        menuBtn.addEventListener('click', toggleMenu);

        // Cerrar menú al hacer click en un enlace
        const navLinks = mobileMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (!mobileMenu.classList.contains('hidden')) {
                    mobileMenu.classList.add('translate-x-full');

                    setTimeout(() => {
                        mobileMenu.classList.add('hidden');
                    }, 300);

                    menuIconOpen.classList.remove('hidden');
                    menuIconClose.classList.add('hidden');
                    document.body.style.overflow = '';
                }
            });
        });
    }

    // Inicializar cuando los componentes estén cargados
    document.addEventListener('componentsLoaded', initMenu);

    // Fallback: intentar inicializar después de un delay
    setTimeout(initMenu, 500);
})();
