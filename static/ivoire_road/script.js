// Ajoutez ceci à votre fichier script.js
document.addEventListener("DOMContentLoaded", function () {
    const loader = document.getElementById("loader");
    const form = document.querySelector('.flip-card__form');
  
    form.addEventListener('submit', function () {
      // Affichez l'animation de chargement
      loader.style.display = 'block';
    });
  });
