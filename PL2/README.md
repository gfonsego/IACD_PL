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
`docker network create network_app`

2. Check if the network was created
`docker network ls`

3. Run mongoDB container connected with the network
`docker run -d --name mongodb --rm --network network_app mongo`

#### 2. Run the backend container

4. Change the localhost address for mongoDB in the backend app
* From: `mongodb://localhost:27017/course-goals`
* To: `mongodb://mongodb:27017/course-goals`

5. Build backend image with the change in backend code
`docker build -t backend_image .`

6. Run the backend container with network options
`docker run --name backend --rm --network network_app -p 80:80 backend_image`

7. Run the frontend container with network options
`docker run --name frontend --rm --network network_app -p 3001:3000 frontend_image`