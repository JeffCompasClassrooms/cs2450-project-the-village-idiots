function toggleMenu() {
    const menu = document.getElementById('nav-menu');
    const hamburger = document.querySelector('.hamburger');
    menu.classList.toggle('active');

    if (menu.classList.contains('active')) {
        const hamburgerRect = hamburger.getBoundingClientRect();
        menu.style.left = (hamburgerRect.left - 30) + 'px';
        menu.style.top = (hamburgerRect.bottom -5) + 'px';

        setTimeout(() => { document.addEventListener('click', closeMenuOnClickOutside);}, 0);
    } else {
        document.removeEventListener('click', closeMenuOnClickOutside);
    }

    function closeMenuOnClickOutside(event) {
        if (!menu.contains(event.target) && !hamburger.contains(event.target)) {
            menu.classList.remove('active');
            document.removeEventListener('click', closeMenuOnClickOutside);
        }
    }
}
