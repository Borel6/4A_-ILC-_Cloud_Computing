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

function sendTweet() {
    const tweetText = document.getElementById('tweetText').value;

    // Récupérer le pseudo depuis localStorage
    const pseudo = localStorage.getItem('pseudo');

    // Envoi du tweet au serveur Flask
    fetch('http://127.0.0.1:5000/tweet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: pseudo,
            tweet_text: tweetText,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Mettez à jour l'interface utilisateur avec le nouveau tweet si nécessaire
    })
    .catch(error => {
        console.error('Erreur lors de l\'envoi du tweet:', error);
    });

    // Réinitialisation du formulaire
    document.getElementById('tweetForm').reset();
}
