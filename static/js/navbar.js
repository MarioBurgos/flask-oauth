// Obtén los elementos del botón de hamburguesa y del menú móvil
const hamburgerBtn = document.getElementById('hamburger-btn');
const mobileMenu = document.getElementById('mobile-menu');

// Escucha el clic en el botón hamburguesa
hamburgerBtn.addEventListener('click', () => {
    // Alterna la visibilidad del menú móvil
    mobileMenu.classList.toggle('hidden');
});