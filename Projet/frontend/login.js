function login() {
    // Récupérer les informations de connexion du formulaire
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Envoyer une requête API Flask pour vérifier les informations de connexion
    fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        // Vérifier la réponse de l'API Flask
        if (data.success) {
            // Rediriger vers la page projet.html si la connexion est réussie
            localStorage.setItem('pseudo', username);
            window.location.href = "projet.html";
        } else {
            // Afficher un message d'erreur si la connexion échoue
            alert("Nom d'utilisateur ou mot de passe incorrect.");
        }
    })
    .catch(error => {
        console.error('Erreur lors de la requête API:', error);
    });
}
