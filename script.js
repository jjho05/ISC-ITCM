document.addEventListener('DOMContentLoaded', () => {
    // 1. Seleccionar los elementos del DOM
    const menuBtn = document.getElementById('menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIconOpen = document.getElementById('menu-icon-open');
    const menuIconClose = document.getElementById('menu-icon-close');
    const navLinks = mobileMenu.querySelectorAll('a'); // Seleccionar todos los enlaces del menú móvil

    // 2. Función para abrir/cerrar el menú
    const toggleMenu = () => {
        // Alterna la clase 'hidden' en el menú móvil
        mobileMenu.classList.toggle('hidden');
        
        // Alterna la visibilidad de los iconos de hamburguesa y 'X'
        menuIconOpen.classList.toggle('hidden');
        menuIconClose.classList.toggle('hidden');
    };

    // 3. Añadir el evento 'click' al botón del menú
    menuBtn.addEventListener('click', toggleMenu);

    // 4. (Opcional pero recomendado) Cerrar el menú al hacer clic en un enlace
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Solo cierra el menú si está abierto
            if (!mobileMenu.classList.contains('hidden')) {
                toggleMenu();
            }
        });
    });
});