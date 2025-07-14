* Nginx Reverse Proxy Project
This document provides a comprehensive guide to setting up a basic Nginx reverse proxy using Docker and Docker Compose. This project is ideal for understanding fundamental DevOps concepts like containerization, service orchestration, and basic traffic routing.


** 1. Project Overview
This project demonstrates how Nginx can act as a single entry point to route incoming web requests to different backend applications running in separate containers. You will set up:

App 1 (Python Flask): A simple web application serving "Hello from App 1!".

App 2 (Node.js Express): Another simple web application serving "Hello from App 2!".

Nginx Reverse Proxy: This will listen on port 80 and route requests:

Requests to /app1 will be forwarded to App 1.

Requests to /app2 will be forwarded to App 2.

This setup showcases how a reverse proxy simplifies client access to multiple services and provides a foundation for more complex microservices architectures.



** 2. Prerequisite
The only essential prerequisite for this project is Docker Desktop.


** 3. Step-by-Step Guide
Follow these steps to create all the necessary files and directories.

Create App 1 (Python Flask)
Create App 2 (Node.js Express)
Configure Nginx
Create docker-compose.yml

** 4. Running the Project

Execute the following command to build the application images and start all services in detached mode:
docker-compose up --build -d

** 5. Validating Reverse Proxy
Open your web browser and navigate to the following URLs to test the routing:

http://localhost/: You should see the default Nginx welcome message: "Welcome to the Nginx Reverse Proxy! Try /app1 or /app2".

http://localhost/app1: This request will be routed by Nginx to your Python Flask application. You should see: "Hello from App 1!".

http://localhost/app2: This request will be routed by Nginx to your Node.js Express application. You should see: "Hello from App 2!".
