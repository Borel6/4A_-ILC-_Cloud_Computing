import redis

# Connexion à Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def load_default_data():

    

    # Ajout d'utilisateurs par défaut
    users = [
        {'username': 'SoldierBoy', 'password': '2635'},
        {'username': 'Homelander', 'password': '2635'},
        {'username': 'jerome', 'password': '2635'}
    ]
    for user in users:
        user_key = f'id-{user["username"]}'
        redis_client.hmset(user_key, {'username': user['username'], 'password': user['password']})
        redis_client.sadd('usernames', user['username'])

    # Ajout de tweets par défaut
    tweets = [
        {'username': 'jerome', 'tweet_text': 'je suis un sacré #BG barbu quand-même'},
        {'username': 'beyonder', 'tweet_text': 'vous attendez quoi pour regarder The Boys'},
        {'username': 'supremeBeyonder', 'tweet_text': 'un mec a dit hier #BreakingBad est suroté LOL'},
        {'username': 'beyonder', 'tweet_text': 'vous benchez combien vous ?'},
        {'username': 'supremeBeyonder', 'tweet_text': '#DUNE2 le banger de fou'}
    ]
    for tweet in tweets:
        id_tweet = redis_client.incr('tweet_id_counter')
        tweet_key = f'tweet-{id_tweet}'
        redis_client.hmset(tweet_key, {'username': tweet['username'], 'tweet': tweet['tweet_text']})
        redis_client.sadd(tweet['username'], tweet_key)

    # Ajout de hashtags par défaut
    hashtags = ['MESSI', 'MESSIGOAT','DUNE2','BreakingBad', 'BG']
    for hashtag in hashtags:
        hashtag_key = redis_client.incr('hashtag_id_counter')
        hashtag_key = f'hashtag-{hashtag_key}'
        redis_client.set(hashtag_key, hashtag)

if __name__ == '__main__':
    load_default_data()
    print("Données par défaut chargées avec succès dans la base de données Redis.")
