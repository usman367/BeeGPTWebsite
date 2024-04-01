// Utilised briancodex's public GitHub repository (last accessed: 31/03/2024) for a responsive navbar
// Available at: https://github.com/briancodex/html-css-js-website-smooth-scroll
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



// For the image slideshow on the home page
// Utilised this example (last accessed: 31/03/2024): https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_slideshow_auto
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    slides[i].style.opacity = "0";
  }
  slideIndex++;

  if (slideIndex > slides.length) {
    slideIndex = 1
  }
  slides[slideIndex-1].style.display = "block";
  setTimeout(function() { slides[slideIndex-1].style.opacity = "1"; }, 100); // Start fade in effect
  setTimeout(showSlides, 4000); // Change image every 4 seconds
}