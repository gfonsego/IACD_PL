# PL2

## Objectives
1. Connect banckend component with database
2. connect frontend component with backend component
3. Persist data from Database
4. Persist data from NodeJS Web App

## Steps and Command Lines

### Running with docker network

#### 1. Run MongoDB container

1. Create docker network
`sudo docker network create my_app`

2. Check if the network was created
`sudo docker network ls`

3. Run mongoDB container connected with the network and volumes options 
`sudo docker run -d --name mongodb --rm --network my_app -v my_volume:/data/db mongo`

#### 2. Run Multi-container App

4. Change the localhost address for mongoDB in the backend app
* From: `mongodb://localhost:27017/course-goals`
* To: `mongodb://mongodb:27017/course-goals`

5. Build backend image with the change in backend code
`sudo docker build -t my_backend_image .`

6. Run the backend container with network and volumes options
`sudo docker run --name backend --rm --network my_app -p 80:80 -v my_volume:/app/backend my_backend_image`

7. Run the frontend container with network options
`sudo docker run --name frontend --rm --network my_app -p 3000:3000 my_frontend_image`

8. Stop backend conteiner 
`sudo docker stop backend`

9. Stop mongodb 
`sudo docker stop mongodb`