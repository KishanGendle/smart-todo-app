# Smart ToDo App

A simple Full Stack ToDo Application built using Flask and MongoDB.

This application allows users to:
- Register/Login
- Add Tasks
- Edit Tasks
- Complete Tasks
- Delete Tasks
- Search Tasks

The project is beginner-friendly and follows a clean folder structure.

---

# Tech Stack

## Frontend
- HTML
- CSS
- Bootstrap 5
- Jinja2 Templates

## Backend
- Flask

## Database
- MongoDB

---

# Features

## Authentication
- User Registration
- User Login
- User Logout
- Password Hashing using bcrypt
- Session Management

## Task Management
- Add Task
- Edit Task
- Complete Task
- Delete Task
- Search Tasks

## UI Features
- Responsive Design
- Bootstrap Cards
- Flash Messages
- Clean Dashboard UI

---

# Installation Steps

## 1. Clone Repository

git clone <your-github-repo-url>

cd todo-app

---

## 2. Create Virtual Environment

### Windows
```text
python -m venv venv

venv\Scripts\activate
```
### Linux/Mac
```
python3 -m venv venv

source venv/bin/activate
```
---

## 3. Install Dependencies
```
pip install -r requirements.txt
```
---

# Environment Variables
```
Create a .env file in the root directory.

Example:

MONGO_URI=mongodb://localhost:27017/todoapp

SECRET_KEY=mysecretkey
```
---

# MongoDB Setup
```
Make sure MongoDB is installed and running locally.

Default MongoDB Port:

27017
```
---

# Run Application
```
python app.py
```
---

# Open Browser
```text
http://127.0.0.1:5000
```
---

# Kubernetes Setup

## Apply Namespace
```text
kubectl apply -f k8s/namespace.yaml
```
## Apply ConfigMap & Secret
```text
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
```
## Apply PV & PVC
```text
kubectl apply -f k8s/mongodb-pv.yaml
kubectl apply -f k8s/mongodb-pvc.yaml
```
## Deploy MongoDB
```text
kubectl apply -f k8s/mongodb-deployment.yaml
kubectl apply -f k8s/mongodb-service.yaml
```
## Deploy Flask App
```text
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
## Enable Ingress
```text
minikube addons enable ingress
```
## Apply Ingress
```text
kubectl apply -f k8s/ingress.yaml
```
# Verify Resources

## Pods
```text
kubectl get pods -n todo-app
```


## Services
```text
kubectl get svc -n todo-app
```
## Ingress
```text
kubectl get ingress -n todo-app
```
---

# Python Libraries Used

- flask
- flask-pymongo
- flask-session
- bcrypt
- python-dotenv

---

# Security Features

- Password hashing using bcrypt
- Session-based authentication
- Protected routes

---

# Future Improvements

- Docker Support
- Kubernetes Deployment
- Dark Mode
- Task Due Dates
- Pagination
- REST APIs
- JWT Authentication

---
