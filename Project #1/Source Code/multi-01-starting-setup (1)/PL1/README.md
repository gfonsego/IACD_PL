# 1. Install Docker

Use the following commanda line
`docker --version`

# 2. Create Docker Images

1. Pull the NODE base image
`docker pull node`

2. Create a Dockerfile with configurations for Backend and Frontend
3. Write the configs in the dockerfile

4. Build image for Backend
`docker build -t backend_image .`

5. Build Image for Frontend
`docker build -t frontend_image .`

6. Pull MongoDB image
`docker pull mongo`

7. Run MongoDB container
`docker run -d --name mongodb -p 27017:27017 mongo`

8. Run Frontend container
`docker run -d --name frontend -p 3000:3000 frontend_image`

9. Run Backend container
`docker run -d --name backend -p 80:80 backend_image`


# 3. Other Docker Commands

Show the log of error when trying to run a container
`docker logs backend`

Stop containers
`docker stop backend`

Exclude containers
`docker rm backend`

Exclude images
`docker rmi backend_image`