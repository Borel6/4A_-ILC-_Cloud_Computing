function signup() {
    // Récupérez les informations d'inscription du formulaire
    const newUsername = document.getElementById('newUsername').value;
    const newPassword = document.getElementById('newPassword').value;

    // Envoyez une requête API Flask pour enregistrer le nouvel utilisateur
    fetch('http://127.0.0.1:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: newUsername, password: newPassword }),
    })
    .then(response => response.json())
    .then(data => {
        // Vérifiez la réponse de l'API Flask
        if (data.success) {
            // Affichez un message de succès ou redirigez vers la page de connexion, etc.
            alert("Inscription réussie. Vous pouvez maintenant vous connecter.");
            window.location.href = "index.html";  // Redirection vers la page de connexion
        } else {
            // Affichez un message d'erreur si l'inscription échoue
            alert("Erreur lors de l'inscription: " + data.message);
        }
    })
    .catch(error => {
        console.error('Erreur lors de la requête API:', error);
    });
}
