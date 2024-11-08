1. Change the address for mongoDB in the backend app
* From: `mongodb://mongodb:27017/course-goals`
* To: `'mongodb://mongo-service:27017/course-goals` where mongo-service is the name defined in the mongodb-service.yaml file.

2. Build backend image with the changes in the backend code:
`docker build -t jmbp75/iacd_pl4_backend .`

3. Push backend image with the changes in the backend code:
`docker push jmbp75/iacd_pl4_backend`

4. Apply deployments and services
`kubectl apply -f=backend-deployment.yaml`
`kubectl apply -f=backend-service.yaml`
`kubectl apply -f=mongodb-deployment.yaml`
`kubectl apply -f=mongodb-service.yaml`

5. Create backend file for persistence.

6. Deploy backend file for persistence:
`kubectl apply -f=backend_pv.yaml`

7. Create backend file for consistency:
   
8. Deploy backend file for consistency:
`kubectl apply -f=backend_pvc.yaml`

9. Create mongodb file for persistence.

10. Deploy mongodb file for persistence:
`kubectl apply -f=mongo_pv.yaml`

11. Create mongodb file for consistency.

12. Deploy mongodb file for consistency:
`kubectl apply -f=mongo_pvc.yaml`

13. Find backend url: 
`minikube service backend-service --url`
  
14. Copy the ip and change the source code in the frontend app:
* From `http://localhost/goals` 
* To `http://**Ip found in the previous command**/goals`

15. Build frontend image with the changes in the frontend code:
`docker build -t jmbp75/iacd_pl4 .`

16. Push frontend image with the changes in the frontend code:
`docker push jmbp75/iacd_pl4`

17. Apply deployments and services for the frontend
`kubectl apply -f=frontend-deployment.yaml`
`kubectl apply -f=frontend-service.yaml`

18. Open the App
`minikube service frontend-service`