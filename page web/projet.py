from flask import Flask, request, jsonify
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json  # Assurez-vous d'envoyer les données en tant que JSON depuis votre front-end
    username = data.get('username')
    password = data.get('password')

    # Vérifiez si le nom d'utilisateur est déjà pris
    if redis_client.sismember('usernames', username):
        return jsonify({"message": "Nom d'utilisateur déjà pris. Veuillez en choisir un autre."}), 400

    # Enregistrez les informations de l'utilisateur dans Redis
    user_id = redis_client.incr('user_id_counter')
    user_key = f'id-{username}'
    redis_client.hmset(user_key, {'id': user_id, 'username': username, 'password': password})
    redis_client.sadd('usernames', username)

    return jsonify({"message": "Utilisateur enregistré avec succès"}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json  # Assurez-vous d'envoyer les données en tant que JSON depuis votre front-end
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

if __name__ == '__main__':
    app.run(debug=True)
