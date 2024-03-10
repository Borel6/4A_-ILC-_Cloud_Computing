document.addEventListener("DOMContentLoaded", function () {
    // on réccup le pseudo depuis localStorage
    const pseudo = localStorage.getItem('pseudo');

    // on Remplit la section du profil avec le pseudo
    const profileSection = document.getElementById('profile');
    profileSection.innerHTML = `
    <h2>Profil</h2>
    <div class = pdp>
        <img src="/projet/img/${pseudo}.webp" alt="Avatar" >
        <p>Pseudo: ${pseudo}</p>
        <p >Description: <span id="descriptionValue">Description: cette description est definie par défaut pour tous les utilisateurs <br> Messi is hte GOAT</span></p>
    
    <div/>
        
       `;

    // Fetch user's tweets
    fetchUserTweets(pseudo);
});

function fetchUserTweets(username) {
    fetch(`http://127.0.0.1:5000/tweets/${username}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const tweets = data.tweets;
                const tweetSection = document.getElementById('tweetList');
                tweetSection.innerHTML = ''; // on efface les tweets deja affichés

                tweets.forEach(tweet => {
                    const tweetDiv = document.createElement('div');
                    tweetDiv.classList.add('tweet');

                    const tweetContentDiv = document.createElement('div');
                    tweetContentDiv.classList.add('tweet-content');

                    const tweetTextParagraph = document.createElement('p');
                    tweetTextParagraph.classList.add('tweet-text');
                    tweetTextParagraph.textContent = `@${tweet.username}: ${tweet.tweet_text}`;

                    tweetContentDiv.appendChild(tweetTextParagraph);
                    tweetDiv.appendChild(tweetContentDiv);

                    tweetSection.appendChild(tweetDiv); // Append the tweet to the tweet section
                });
            }
        })
        .catch(error => {
            console.error('Error fetching user tweets:', error);
        });
}
