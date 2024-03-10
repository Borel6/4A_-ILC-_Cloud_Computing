from flask import Flask, request, jsonify
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json  #on s'assure d'envoyer les données en tant que JSON depuis votre front-end
    username = data.get('username')
    password = data.get('password')

    # Vérifie si le nom d'utilisateur est déjà pris
    if redis_client.sismember('usernames', username):
        return jsonify({"message": "Nom d'utilisateur déjà pris. Veuillez en choisir un autre."}), 400

    # Enregistre les informations de l'utilisateur dans Redis
    
    user_key = f'id-{username}'
    redis_client.hmset(user_key, {'username': username, 'password': password})
    redis_client.sadd('usernames', username)

    return jsonify({"message": "Utilisateur enregistré avec succès"}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json  #on s'assure d'envoyer les données en tant que JSON depuis votre front-end
    username = data.get('username')
    password = data.get('password')

    user_key = f'id-{username}'

    # Vérifiez si le nom d'utilisateur existe dans Redis
    if not redis_client.exists(user_key):
        return jsonify({"success": False, "message": "Nom d'utilisateur incorrect"}), 401

    # Récupérez les informations de l'utilisateur depuis Redis
    user_info = redis_client.hgetall(user_key)

    # Vérifiez si le mot de passe correspond
    if password == user_info[b'password'].decode():
        return jsonify({"success": True, "message": "Connexion réussie"}), 200
    else:
        return jsonify({"success": False, "message": "Mot de passe incorrect"}), 401
    
@app.route('/tweet', methods=['POST'])
def tweet():
    try:
        data = request.get_json()
        username = data.get('username')
        tweet_text = data.get('tweet_text')


        # on extrait le hashtag
        hashtags = [word for word in tweet_text.split() if word.startswith('#')]
        # on verifie si il y a des hashtags
        if hashtags:
            # Store each hashtag in Redis
            for hashtag in hashtags:
                hashtag_key = redis_client.incr('hashtag_id_counter')
                hashtag_key = f'hashtag-{hashtag_key}'
                redis_client.set(hashtag_key, hashtag)
        
        id_tweet = redis_client.incr('tweet_id_counter')
        tweet_key = f'tweet-{id_tweet}'

        redis_client.hmset(tweet_key, {'username': username, 'tweet': tweet_text})
        redis_client.sadd(username, tweet_key)

        return jsonify({"success": True, "message": "Tweet enregistré avec succès","hashtag": hashtag}), 201
    except Exception as e:
        print(f"Erreur lors de la gestion de la requête : {str(e)}")
        return jsonify({"success": False, "message": "Erreur lors de la gestion de la requête"}), 500


@app.route('/tweets', methods=['GET'])
def get_tweets():
    try:
        # on récupère les clés des tweets et retweets
        tweet_keys = redis_client.keys('tweet-*')

        # on crée un tableau de tweets
        tweets = []

        # on boucle et on remplit le tableau avec les tweets et les retweets
        for tweet_key in tweet_keys:
            tweet_data = redis_client.hgetall(tweet_key)
            tweet = {
                'username': tweet_data[b'username'].decode(),
                'tweet_text': tweet_data[b'tweet'].decode()
            }
            # Si le tweet a un champ 'retweeter' alors c'est un retweet donc on l'add
            if b'retweeter' in tweet_data:
                tweet['retweeter'] = tweet_data[b'retweeter'].decode()
            tweets.append(tweet)

        return jsonify({"success": True, "tweets": tweets}), 200
    except Exception as e:
        print(f"Error fetching tweets: {str(e)}")
        return jsonify({"success": False, "message": "Erreur d'affichage"}), 500


@app.route('/tweets/<username>', methods=['GET'])
def get_user_tweets(username):
    try:
        # on veifie si l'user existe
        if not redis_client.exists(f'id-{username}'):
            return jsonify({"success": False, "message": "utilisateur innexistant"}), 404

        # on reccup tous ses tweets
        tweet_keys = redis_client.smembers(username)
        tweets = []

        # onremplit le tableau de tweets et on le renvoie au compte.js
        for tweet_key in tweet_keys:
            tweet_data = redis_client.hgetall(tweet_key)
            tweet = {
                'username': tweet_data[b'username'].decode(),
                'tweet_text': tweet_data[b'tweet'].decode()
            }
            tweets.append(tweet)

        return jsonify({"success": True, "tweets": tweets}), 200
    except Exception as e:
        print(f"Error fetching user tweets: {str(e)}")
        return jsonify({"success": False, "message": "Error d'affichage"}), 500


@app.route('/retweets', methods=['POST'])
def retweet():
    try:
        data = request.get_json()
        username = data.get('username')
        retweeter = data.get('Retweeter')
        tweet_text = data.get('tweet_text')
        
        id_tweet = redis_client.incr('tweet_id_counter')
        tweet_key = f'tweet-{id_tweet}'

        # on crée le retweet de manière à ce qu'il soit traité 
        redis_client.hmset(tweet_key, {'username': username, 'tweet': tweet_text, 'retweeter': retweeter})
        redis_client.sadd(retweeter, tweet_key)

        return jsonify({"success": True, "message": "reTweet enregistré avec succès"}), 201
    except Exception as e:
        print(f"Erreur lors de la gestion de la requête : {str(e)}")
        return jsonify({"success": False, "message": "Erreur lors de la gestion de la requête"}), 500


    
@app.route('/hashtags', methods=['GET'])
def get_hashtags():
    try:
        # Récupérer tous les hashtags stockés dans Redis
        hashtag_keys = redis_client.keys('hashtag-*')

        # Créer un ensemble pour stocker des hashtags uniques
        hashtags = set()

        for hashtag_key in hashtag_keys:
            hashtag = redis_client.get(hashtag_key).decode()
            hashtags.add(hashtag)

        return jsonify({"success": True, "hashtags": list(hashtags)}), 200
    except Exception as e:
        print(f"Error fetching hashtags: {str(e)}")
        return jsonify({"success": False, "message": "Erreur lors de la récupération des hashtags"}), 500

if __name__ == '__main__':
    app.run(debug=True)
