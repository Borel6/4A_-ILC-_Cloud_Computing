
FROM python:3.12
COPY . /appDocker
WORKDIR /appDocker
RUN pip install Flask

CMD ["python", "projet.py"]

# Dockerfile du FRONTEND
# docker build -t frontend:latest .
# docker run -p 80:8080 frontend

# Image de base avec un serveur web
FROM nginx

WORKDIR /usr/share/nginx/html
COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]