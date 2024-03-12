
## Fonctionnalités du frontend

### 1. Affichage et Interaction Générale

- **Navigation :**
  - L'utilisateur peut cliquer sur l'icône d'accueil pour revenir à la page principale où tous les tweets sont affichés.
  - L'icône de profil permet à l'utilisateur d'accéder à son profil où ses propres tweets sont affichés.
  - Les autres icônes (par exemple, recherche, notifications) sont décoratives et n'ont pas de fonctionnalités spécifiques dans cette version.

### 2. Affichage des Tweets

- **Affichage des Tweets :**
  - Tous les tweets disponibles sont affichés sur la page principale du projet.
  - Chaque tweet affiche l'avatar de l'utilisateur, le nom d'utilisateur, le texte du tweet, et le cas échéant, des informations sur le retweeteur.
  - L'utilisateur peut retweeter un tweet en cliquant sur le bouton "Retweet". Cela ajoute une nouvelle entrée dans la base de données avec le tweet original et le nom de l'utilisateur actuellement connecté.

### 3. Gestion de l'Authentification

- **Connexion :**
  - L'utilisateur peut saisir son nom d'utilisateur et son mot de passe dans le formulaire de connexion pour se connecter à son compte.
  - En cas de succès, l'utilisateur est redirigé vers la page principale où tous les tweets sont affichés.
  - En cas d'échec, un message d'erreur est affiché indiquant que le nom d'utilisateur ou le mot de passe est incorrect.

- **Inscription :**
  - L'utilisateur peut s'inscrire en fournissant un nouveau nom d'utilisateur et un mot de passe.
  - En cas de succès, l'utilisateur est redirigé vers la page de connexion où il peut se connecter avec ses nouvelles informations.
  - En cas d'échec (par exemple, nom d'utilisateur déjà pris), un message d'erreur approprié est affiché.

### 4. Profil Utilisateur

- **Affichage du Profil :**
  - L'utilisateur peut accéder à son profil en cliquant sur l'icône de profil.
  - Sur la page du profil, l'utilisateur peut voir ses propres tweets, son nom d'utilisateur et son avatar.
  - Une description par défaut est affichée pour tous les utilisateurs.

### 5. Gestion des Retweets

- **Retweets :**
  - L'utilisateur peut retweeter un tweet en cliquant sur le bouton "Retweet".
  - Lorsqu'un tweet est retweeté, une nouvelle entrée est ajoutée à la base de données, avec une référence au tweet original et au nom de l'utilisateur qui a retweeté.
  - Les retweets sont identifiés sur l'interface utilisateur par une indication spécifique dans le contenu du tweet.

### 6. Gestion des Photos de Profil

- **Photos de Profil :**
  - Chaque utilisateur possède une photo de profil associée à son compte.
  - Les photos de profil sont stockées sur le serveur et sont accessibles via une URL spécifique.
  - Lorsqu'un utilisateur publie un tweet ou retweet, son avatar est affiché à côté de son nom d'utilisateur dans le contenu du tweet.
  - Les photos de profil sont récupérées et affichées dynamiquement sur l'interface utilisateur en fonction du nom d'utilisateur associé à chaque tweet.

Ces fonctionnalités offrent à l'utilisateur une expérience complète de navigation, de partage et d'interaction sur la plateforme, en incluant la possibilité de retweeter des tweets et de personnaliser son profil avec une photo.