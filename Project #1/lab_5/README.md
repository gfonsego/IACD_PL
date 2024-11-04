1. Change the localhost address for mongoDB in the backend app
* From: `mongodb://mongodb:27017/course-goals`
* To: `'mongodb://mongo-service:27017/course-goals` where mongo-service is the name defined in the mongodb-service.yaml file.

2. Build and push backend image with the changes in the backend code
* docker build -t jmbp75/iacd_pl4_backend .
* docker push jmbp75/iacd_pl4_backend

3. Apply deployments and services
* kubectl apply -f=backend-deployment.yaml
* kubectl apply -f=backend-service.yaml
* kubectl apply -f=backend_pvc.yaml
* kubectl apply -f=backend-pv.yaml
* kubectl apply -f=mongodb-deployment.yaml
* kubectl apply -f=mongodb-service.yaml
* kubectl apply -f=mongodb-pvc.yaml
* kubectl apply -f=mongodb-pv.yaml

4. Find backend url 
* minikube service backend-service --url
  
5. Copy the ip and change the source code in the frontend app
* From `http://localhost/goals` 
* To `http://**Ip found in the previous command**/goals`

6. Build and push frontend image with the changes in the frontend code
* docker build -t jmbp75/iacd_pl4 .
* docker push jmbp75/iacd_pl4

7. Apply deployments and services
* kubectl apply -f=frontend-deployment.yaml
* kubectl apply -f=frontend-service.yaml

8. Open the App
* minikube service frontend-service