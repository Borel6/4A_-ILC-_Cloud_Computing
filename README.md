# 4A_-ILC-_Cloud_Computing
# Flask Twitter API

Cette API simple a été développée en utilisant Flask et Redis pour permettre l'enregistrement d'utilisateurs, la publication de tweets, et la gestion des retweets. Elle fournit également des fonctionnalités telles que la récupération des tweets, des hashtags, et des tweets spécifiques à un utilisateur.

# Routes API

## 1. Enregistrement d'utilisateur

- **URL :** `/register`
- **Méthode :** `POST`
- **Description :** Enregistre un nouvel utilisateur avec un nom d'utilisateur unique.
- **Paramètres requis :** `username` (nom d'utilisateur), `password` (mot de passe).
- **Réponses :**
  - 201 OK: Utilisateur enregistré avec succès.
  - 400 Bad Request: Nom d'utilisateur déjà pris.

## 2. Connexion d'utilisateur

- **URL :** `/login`
- **Méthode :** `POST`
- **Description :** Connecte un utilisateur en vérifiant le nom d'utilisateur et le mot de passe.
- **Paramètres requis :** `username` (nom d'utilisateur), `password` (mot de passe).
- **Réponses :**
  - 200 OK: Connexion réussie.
  - 401 Unauthorized: Nom d'utilisateur ou mot de passe incorrect.

## 3. Publication de tweet

- **URL :** `/tweet`
- **Méthode :** `POST`
- **Description :** Permet à un utilisateur de publier un tweet, enregistrant également les hashtags présents.
- **Paramètres requis :** `username` (nom d'utilisateur), `tweet_text` (contenu du tweet).
- **Réponses :**
  - 201 OK: Tweet enregistré avec succès.
  - 500 Internal Server Error: Erreur lors de la gestion de la requête.

## 4. Récupération des tweets

- **URL :** `/tweets`
- **Méthode :** `GET`
- **Description :** Récupère tous les tweets et retweets présents dans le système.
- **Réponses :**
  - 200 OK: Récupération réussie.
  - 500 Internal Server Error: Erreur d'affichage.

## 5. Récupération des tweets d'un utilisateur

- **URL :** `/tweets/<username>`
- **Méthode :** `GET`
- **Description :** Récupère tous les tweets d'un utilisateur spécifique.
- **Paramètres requis :** `username` (nom d'utilisateur).
- **Réponses :**
  - 200 OK: Récupération réussie.
  - 404 Not Found: Utilisateur inexistant.
  - 500 Internal Server Error: Erreur d'affichage.

## 6. Retweet

- **URL :** `/retweets`
- **Méthode :** `POST`
- **Description :** Permet à un utilisateur de retweeter un tweet existant.
- **Paramètres requis :** `username` (nom d'utilisateur), `Retweeter` (nom de l'utilisateur retweetant), `tweet_text` (contenu du tweet).
- **Réponses :**
  - 201 OK: Retweet enregistré avec succès.
  - 500 Internal Server Error: Erreur lors de la gestion de la requête.

## 7. Récupération des hashtags

- **URL :** `/hashtags`
- **Méthode :** `GET`
- **Description :** Récupère tous les hashtags uniques présents dans les tweets.
- **Réponses :**
  - 200 OK: Récupération réussie.
  - 500 Internal Server Error: Erreur lors de la récupération des hashtags.


## Statuts actions
![push-action](https://github.com/Borel6/4A_-ILC-_Cloud_Computing/actions/workflows/build_on_push.yml/badge.svg)
![push-action](https://github.com/Borel6/4A_-ILC-_Cloud_Computing/actions/workflows/build_img.yml/badge.svg)