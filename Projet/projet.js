document.addEventListener("DOMContentLoaded", function () {
    // Récupérer le pseudo depuis localStorage
    const pseudo = localStorage.getItem('pseudo');

    // Remplir la section du profil avec le pseudo
    const profileSection = document.getElementById('profileSection');
    profileSection.innerHTML = `
        <h2>Profil</h2>
        <p>Pseudo: ${pseudo}</p>
        <!-- Ajoutez d'autres informations de profil si nécessaire -->
    `;
});