# Mongo
-   sudo docker pull mongo
-   docker run -d --name mongodb -p 27017:27017 mongo

# Backend

-   sudo docker pull node
-   sudo docker build -t my_backend_image .
-   sudo docker run -d --name backend -p 80:80 my_backend_image

# Frontend

-   sudo docker build -t my_frontend_image .
-   sudo docker run -d --name frontend -p 3000:3000 my_frontend_image
