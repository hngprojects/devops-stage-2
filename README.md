# Full-Stack FastAPI and React Template

Welcome to the Full-Stack FastAPI and React template repository. This repository serves as a demo application for interns, showcasing how to set up and run a full-stack application with a FastAPI backend and a ReactJS frontend using ChakraUI.

## Project Structure

This repository is organized into two main directories from the root folder:

- **frontend**: this folder Contains the ReactJS application, including the docker file added after the fork.
- **backend**: Contains the FastAPI application with the addition of a docker file for building a backend image
- For this project, I will be using a remote DB on Azure for my database needs.

Each directory has its own README file with detailed instructions to set up and run the application locally without a need for containers.

## To run this application locally, please see the read me files below
- [Frontend README](./frontend/README.md)
- [Backend README](./backend/README.md)


## Prerequisites
- Docker
- Docker Compose

### Services needed to run and build this application in containers.
- This repository contains a full-stack application setup using Docker Compose. 
- The application consists of a FastAPI backend, a Node.js frontend, a PostgreSQL database, an Adminer database management tool, an Nginx Proxy Manager, and an Nginx web server.

**Your DB can be self hosted or a remote DB on a cloud service**

- **backend**: FastAPI application serving the backend API.
- **frontend**: Node.js application serving the frontend.
- **Postgres db**: PostgreSQL database for storing application data.
- **adminer**: Database management tool to interact with the PostgreSQL database.
- **proxy**: Nginx Proxy Manager to handle SSL certificates and domain management.
- **nginx**: Nginx web server to serve the frontend and reverse proxy requests to the backend.
- **Docker files**:this will specify how the images will be built and run by docker

## Application Deployment with Docker.

**Clone the repository**:

   ```sh
   git clone https://github.com/Eben-DevOps/Full-Stack-Web-App
   cd Full-Stack-Web-App
   ```

 **Build and start the services** (detached mode is optional):

   ```sh
   docker-compose build
   docker-compose up -d
   ```

 **Verify the services are running**:
   - **FastAPI Backend**: [http://localhost/api](http://localhost/api)
   - **Node.js Frontend**: [http://localhost](http://localhost)
   - **Azure PostgreSQL Database**: Accessible on port `5432` (no direct browser access)
   - **Adminer**: [http://localhost:8080](http://localhost:8080) or [http://db.localhost](http://db.localhost)
   - **Nginx Proxy Manager**: [http://localhost:8090](http://localhost:8090) or [http://proxy.localhost](http://proxy.localhost)

## for my deployment my docker-compose file looks like this
- **note that i used a remote db as you will no see a a db service on this**
```sh
version: '3.8'

services:
  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: frontend
    ports:
      - "5173:5173"
    env_file:
      - ./frontend/.env
    volumes:
      - ./frontend:/app
      - /app/node_modules

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: backend
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    environment:
      PYTHONDONTWRITEBYTECODE: 1
      PYTHONUNBUFFERED: 1
      PYTHONPATH: /app
    volumes:
      - ./backend:/app

  adminer:
    image: adminer
    container_name: adminer
    ports:
      - "8080:8080"

  nginx-proxy-manager:
    image: jc21/nginx-proxy-manager:latest
    container_name: nginx-proxy-manager
    ports:
      - "80:80"     # Nginx Proxy Manager handles HTTP on port 80
      - "8090:81"
      - "443:443"   # Assuming Nginx Proxy Manager's management UI runs on port 81
    env_file:
      - .env
    environment:
      DB_PG_HOST: ${DB_PG_HOST}
      DB_PG_PORT: ${DB_PG_PORT}
      DB_PG_USER: ${DB_PG_USER}
      DB_PG_PASSWORD: ${DB_PG_PASSWORD}
      DB_PG_NAME: ${DB_PG_NAME}
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
    restart: always
```

## Accessing the Application

- **Localhost**: You can access the application via `http://localhost`.
- **Custom Domain**: You can set up your domain to connect to the application using the Nginx Proxy Manager.
