# Dockerfile du BACKEND

# docker build -t backend .
# docker run -d -p 5000:5000 -p 6379:6379 backend

# Utiliser l'image de Python 3.8 comme image de base
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le code source de l'application Flask dans le conteneur
COPY . /app


# Installer Redis
RUN apt-get update && apt-get install -y redis-server

# Exposer le port 5000 pour l'application Flask
EXPOSE 5000

# Exposer le port 6379 pour Redis
EXPOSE 6379


# Commande pour démarrer l'application Flask et le receiver de la queue RabbitMQ
# et l'exécution du fichier defaultUsers.py
CMD ["sh", "-c", "projet.py & python initialize.py"]