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

    displayTweet()
});


function displayTweet(){
   
   fetch('http://127.0.0.1:5000/tweets')
   .then(response => response.json())
   .then(data => {
       if (data.success) {
           const tweets = data.tweets;
           const tweetSection = document.querySelector('.tweets');
           tweetSection.innerHTML = ''; // on efface les tweets existants

           tweets.forEach(tweet => {
               const tweetDiv = document.createElement('div');
               tweetDiv.classList.add('tweet');

               const profilePicDiv = document.createElement('div');
               profilePicDiv.classList.add('profile-pic'); // pour la pdp
               profilePicDiv.style.backgroundColor = '#ccc';

               const tweetContentDiv = document.createElement('div');
               tweetContentDiv.classList.add('tweet-content');

               const usernameHeading = document.createElement('h3');
               usernameHeading.classList.add('username');
               usernameHeading.textContent = tweet.username;

               const tweetTextParagraph = document.createElement('p');
               tweetTextParagraph.classList.add('tweet-text');
               tweetTextParagraph.textContent = tweet.tweet_text;

               tweetContentDiv.appendChild(usernameHeading);
               tweetContentDiv.appendChild(tweetTextParagraph);

               tweetDiv.appendChild(profilePicDiv);
               tweetDiv.appendChild(tweetContentDiv);

               tweetSection.appendChild(tweetDiv); 
               
           });
       }
   })
   .catch(error => {
       console.error('Error fetching tweets:', error);
   });
}


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

        if (data.message== "Tweet enregistré avec succès") {

            const tweetSection = document.querySelector('.tweets');

            const tweetDiv = document.createElement('div');
            tweetDiv.classList.add('tweet');

            const profilePicDiv = document.createElement('div');
            profilePicDiv.classList.add('profile-pic');
            
            
            profilePicDiv.style.backgroundColor = '#ccc'; 

            const tweetContentDiv = document.createElement('div');
            tweetContentDiv.classList.add('tweet-content');

            const usernameHeading = document.createElement('h3');
            usernameHeading.classList.add('username');
            usernameHeading.textContent = pseudo;

            const tweetTextParagraph = document.createElement('p');
            tweetTextParagraph.classList.add('tweet-text');
            tweetTextParagraph.textContent = tweetText;

            tweetContentDiv.appendChild(usernameHeading);
            tweetContentDiv.appendChild(tweetTextParagraph);

            tweetDiv.appendChild(profilePicDiv);
            tweetDiv.appendChild(tweetContentDiv);

            tweetSection.prepend(tweetDiv); 
        
        }

    })
    .catch(error => {
        console.error('Erreur lors de l\'envoi du tweet:', error);
    });

    // Réinitialisation du formulaire
    document.getElementById('tweetForm').reset();
}

function logout() {
    // Clear localStorage (assuming you stored the user information there)
    localStorage.clear();

    // Redirect to index.html
    window.location.href = 'index.html';
}
