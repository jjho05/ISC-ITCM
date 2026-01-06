// Simple Mobile Menu - ISC-ITCM
console.log('🔧 Loading mobile menu...');

window.addEventListener('DOMContentLoaded', function () {
    setTimeout(initMenu, 500);
});

document.addEventListener('componentsLoaded', function () {
    console.log('🎯 Components loaded, initializing menu...');
    initMenu();
});

function initMenu() {
    const navToggle = document.getElementById('menu-btn');
    const navMenu = document.getElementById('mobile-menu');
    const menuIconOpen = document.getElementById('menu-icon-open');
    const menuIconClose = document.getElementById('menu-icon-close');

    console.log('navToggle:', navToggle);
    console.log('navMenu:', navMenu);
    console.log('menuIconOpen:', menuIconOpen);
    console.log('menuIconClose:', menuIconClose);

    if (!navToggle || !navMenu || !menuIconOpen || !menuIconClose) {
        console.error('❌ Menu elements not found!');
        return;
    }

    console.log('✅ Menu elements found!');

    // Toggle menu with transition
    navToggle.onclick = function (e) {
        e.preventDefault();
        e.stopPropagation();

        const isHidden = navMenu.classList.contains('hidden');
        console.log('Menu toggled:', isHidden ? 'opening' : 'closing');

        if (isHidden) {
            // Abrir menú con transición
            navMenu.classList.remove('hidden');
            // Forzar reflow
            navMenu.offsetHeight;
            navMenu.classList.remove('translate-x-full');

            menuIconOpen.classList.add('hidden');
            menuIconClose.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        } else {
            // Cerrar menú con transición
            navMenu.classList.add('translate-x-full');

            setTimeout(() => {
                navMenu.classList.add('hidden');
            }, 300);

            menuIconOpen.classList.remove('hidden');
            menuIconClose.classList.add('hidden');
            document.body.style.overflow = '';
        }
    };

    // Close on link click
    const links = navMenu.querySelectorAll('a');
    links.forEach(link => {
        link.onclick = function () {
            navMenu.classList.add('translate-x-full');

            setTimeout(() => {
                navMenu.classList.add('hidden');
            }, 300);

            menuIconOpen.classList.remove('hidden');
            menuIconClose.classList.add('hidden');
            document.body.style.overflow = '';
        };
    });

    console.log('✅ Mobile menu initialized!');
}
