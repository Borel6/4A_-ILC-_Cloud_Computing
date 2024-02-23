function login() {
    // Récupérez les informations de connexion du formulaire
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Envoyez une requête API Flask pour vérifier les informations de connexion
    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        // Vérifiez la réponse de l'API Flask
        if (data.success) {
            // Redirigez vers la page projet.html si la connexion est réussie
            window.location.href = "projet.html";
        } else {
            // Affichez un message d'erreur si la connexion échoue
            alert("Nom d'utilisateur ou mot de passe incorrect.");
        }
    })
    .catch(error => {
        console.error('Erreur lors de la requête API:', error);
    });
}
