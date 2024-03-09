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
    user_id = redis_client.incr('user_id_counter')
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
        
        id_tweet = redis_client.incr('tweet_id_counter')
        tweet_key = f'tweet-{id_tweet}'

        redis_client.hmset(tweet_key, {'username': username, 'tweet': tweet_text})
        redis_client.sadd(username, tweet_key)

        return jsonify({"success": True, "message": "Tweet enregistré avec succès"}), 201
    except Exception as e:
        print(f"Erreur lors de la gestion de la requête : {str(e)}")
        return jsonify({"success": False, "message": "Erreur lors de la gestion de la requête"}), 500

if __name__ == '__main__':
    app.run(debug=True)
