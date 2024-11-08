1. docker login

2. Build backend image:
`docker build -t jmbp75/iacd_pl4_backend .`

3. Push backend image to DockerHub:
`docker push jmbp75/iacd_pl4_backend`

4. Build frontend image:
`docker build -t jmbp75/iacd_pl4 .`

5. Push frontend image to DockerHub:
`docker push jmbp75/iacd_pl4`


# Imperative Approach

1. Start minikube to use kubernetes locally:
`minikube start`

2. Create object deployments

#### database mongodb
`kubectl create deployment mongodb-deployment --replicas=1 --image=mongo`

#### backend
`kubectl create deployment backend-deployment --replicas=2 --image=jmbp75/iacd_pl4_backend`

#### frontend
`kubectl create deployment frontend-deployment --replicas=3 --image=jmbp75/iacd_pl4`

3. Check deployments
`kubectl get deployments`

4. Check Pods
`kubectl get pods`


# Declarative Approach 

1. Create a folder named kubernetes to store all the created files.

2. Create backend deployment file.

3. Deploy backend deployment file:
`kubectl apply -f=backend-deployment.yaml`
   
4. Create backend service file

5. Deploy backend service file:
`kubectl apply -f=backend-service.yaml`

6. Create frontend deployment file.

7. Deploy frontend deployment file:
`kubectl apply -f=frontend-deployment.yaml`

8. Create frontend service file.

9. Deploy frontend service file:
`kubectl apply -f=frontend-service.yaml`

10. Create mongodb deployment file.

11. Deploy mongodb deployment file:
`kubectl apply -f=mongodb-deployment.yaml`

12. Create mongodb service file.

13. Deploy mongodb service file:
`kubectl apply -f=mongodb-service.yaml`

14. Check deployments
`kubectl get deployments`

15. Check Pods
`kubectl get pods`