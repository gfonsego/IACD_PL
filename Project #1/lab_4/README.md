** 1- Push Docker Images on DockerHub **

>> docker login

* backend

>> docker build -t jmbp75/iacd_pl4_backend .
>> docker push jmbp75/iacd_pl4_backend

* frontend

>> docker build -t jmbp75/iacd_pl4 .
>> docker push jmbp75/iacd_pl4

* Check images in dockerhub

** 2- Imperative Approach **

>> minikube start

##criar objetos Deployment

* database mongodb

>> kubectl create deployment mongodb-deployment --replicas=1 --image=mongo

* backend

>> kubectl create deployment backend-deployment --replicas=2 --image=jmbp75/iacd_pl4_backend

* frontend

>> kubectl create deployment frontend-deployment --replicas=3 --image=jmbp75/iacd_pl4

>> kubectl get deployments
>> kubectl get pods

>> kubectl expose deployment backend_deployment --type=LoadBalancer --port=80


** 3- Declarative Approach **

* backend 

## criar Deployment File
------- backend-deployment.yaml

## Fazer Deployment

>> kubectl apply -f=backend-deployment.yaml
>> kubectl get deployments
>> kubectl get pods

## criar Service object File
-------- backend-service.yaml

>> kubectl apply -f=backend-service.yaml
>> kubectl get services 

* frontend

## criar Deployment File
------- frontend-deployment.yaml

## Fazer Deployment

>> kubectl apply -f=frontend-deployment.yaml
>> kubectl get deployments
>> kubectl get pods

## criar Service object File
-------- frontnd-service.yaml

>> kubectl apply -f=frontend-service.yaml
>> kubectl get services 

* mongodb

## criar Deployment File
------- mongodb-deployment.yaml

## Fazer Deployment

>> kubectl apply -f=mongodb-deployment.yaml
>> kubectl get deployments
>> kubectl get pods

## criar Service object File
-------- mongodb-service.yaml

>> kubectl apply -f=mongodb-service.yaml
>> kubectl get services 