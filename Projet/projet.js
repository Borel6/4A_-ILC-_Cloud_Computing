document.addEventListener("DOMContentLoaded", function () {
    // Récupérer le pseudo depuis localStorage
    const pseudo = localStorage.getItem('pseudo');

    // Remplir la section du profil avec le pseudo
    const profileSection = document.getElementById('profileSection');
    profileSection.innerHTML = `
        <p>Pseudo: ${pseudo}</p>
        <div class="profile-picture">
            <img src="/projet/img/${pseudo}.webp" alt="Photo de profil">
        </div>
    `;


    displayTweet(pseudo)
});


function displayTweet(pseudo){
   
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


                const profilePicImg = document.createElement('img');
                // on définit l'attribut src de l'image en utilisant le chemin vers l'image
                profilePicImg.src = `/projet/img/${tweet.username}.webp`;
                // on definit l'attribut alt de l'image 
                profilePicImg.alt = `Photo de profil de ${tweet.username}`;
                // on ajoute la classe pour le style CSS
                profilePicImg.classList.add('profile-pic-img');

                // Ajouter l'image à la division de la photo de profil
                profilePicDiv.appendChild(profilePicImg);
               
                

               const tweetContentDiv = document.createElement('div');
               tweetContentDiv.classList.add('tweet-content');

               const usernameHeading = document.createElement('h3');
               usernameHeading.classList.add('username');
               usernameHeading.textContent = tweet.username;

               const tweetTextParagraph = document.createElement('p');
               tweetTextParagraph.classList.add('tweet-text');
               tweetTextParagraph.textContent = tweet.tweet_text;

               // partie retweet
               const retweetButton = document.createElement('button');
                    retweetButton.innerHTML = '<i class="fas fa-retweet"></i> Retweet';
                    retweetButton.classList.add('retweet-button');



                    //on verifie si le boutton est deja cliqué
                    const isRetweeted = localStorage.getItem(`retweet-${tweet.tweet_text}`);
                    console.log(isRetweeted);
                    if (isRetweeted) {
                        
                        retweetButton.classList.add('retweeted');
                    }

                    retweetButton.addEventListener('click', function() {
                        retweetTweet(tweet.username,pseudo, tweet.tweet_text,retweetButton);
                        console.log('Retweet clicked!');
                    });

               tweetContentDiv.appendChild(usernameHeading);
               tweetContentDiv.appendChild(tweetTextParagraph);
               tweetContentDiv.appendChild(retweetButton);
               tweetDiv.appendChild(profilePicDiv);
               tweetDiv.appendChild(tweetContentDiv);

               //on vérifie si le tweet est un retweet
                if (tweet.retweeter) {
                    const retweetInfo = document.createElement('p');
                    retweetInfo.textContent = `Retweeté par: ${tweet.retweeter}`;
                    tweetDiv.insertBefore(retweetInfo, profilePicDiv); 
                }

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




function retweetTweet(username, Retweeter, tweet,retweetButton) {
 // on vérifie si le boutton n'a pas deja été rt
 const isRetweeted = localStorage.getItem(`retweet-${tweet}`);
 if (!isRetweeted) {
    fetch('http://127.0.0.1:5000/retweets', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            Retweeter: Retweeter,
            tweet_text: tweet,
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message);
        retweetButton.classList.add('retweeted');// on modifie la couleur avec le css
        localStorage.setItem(`retweet-${tweet}`, true); // on stock le status du tweet
    })
    .catch(error => {
        console.error('Error retweeting tweet:', error);
    });
}
}