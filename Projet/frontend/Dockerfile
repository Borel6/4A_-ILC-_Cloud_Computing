
# Dockerfile du FRONTEND
# docker build -t frontend:latest .
# docker run -p 80:80 frontend

# Image de base avec un serveur web
FROM nginx

WORKDIR /usr/share/nginx/html
COPY . /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]