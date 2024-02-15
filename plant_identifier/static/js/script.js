const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar-menu');
const navLogo = document.querySelector('#navbar-title');

// Display Mobile Menu
const mobileMenu = () => {
  menu.classList.toggle('is-active');
  menuLinks.classList.toggle('active');
};

menu.addEventListener('click', mobileMenu);


// Close Mobile Menu when clicking on Menu item when its open
// Active = Menu is open
const hideMobileMenu = () => {
    const menuBars = document.querySelector('.is-active');
    if (window.innerWidth <= 768 && menuBars) {
      menu.classList.toggle('is-active');
      menuLinks.classList.remove('active');
    }
  };

  menuLinks.addEventListener('click', hideMobileMenu);
  navLogo.addEventListener('click', hideMobileMenu);