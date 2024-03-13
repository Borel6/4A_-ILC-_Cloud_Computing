# Dockerfile du FRONTEND
# docker build -t frontend .
# docker run -p 80:8080 frontend

# Utiliser l'image NGINX comme image de base
FROM nginx

# Copier les fichiers statiques du frontend dans le répertoire `/usr/share/nginx/html` du conteneur
COPY ./html /usr/share/nginx/html

# Exposer le port 80 pour NGINX
EXPOSE 80

# Commande par défaut pour démarrer NGINX lorsqu'un conteneur est lancé
CMD ["nginx", "-g", "daemon off;"]
