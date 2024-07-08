# Full-Stack FastAPI and React Template

Welcome to the Full-Stack FastAPI and React template repository. This repository serves as a demo application for interns, showcasing how to set up and run a full-stack application with a FastAPI backend and a ReactJS frontend using ChakraUI.

## Project Structure

This repository is organized into two main directories from the root folder:

- **frontend**: this folder Contains the ReactJS application, including the docker file added after the fork.
- **backend**: Contains the FastAPI application with the addition of a docker file for building a backend image
- For this project, I will be using a remote DB on Azure for my database needs.

Each directory has its own README file with detailed instructions to set up and run the application locally without a need for containers. 

To run this application locally, please follow the instructions in the respective directories:
###Services needed to run and build this application locally and in containers.

This repository contains a full-stack application setup using Docker Compose. The application consists of a FastAPI backend, a Node.js frontend, a PostgreSQL database, an Adminer database management tool, an Nginx Proxy Manager, and an Nginx web server.

## Services

- **backend**: FastAPI application serving the backend API.
- **frontend**: Node.js application serving the frontend.
- **db**: PostgreSQL database for storing application data.
- **adminer**: Database management tool to interact with the PostgreSQL database.
- **proxy**: Nginx Proxy Manager to handle SSL certificates and domain management.
- **nginx**: Nginx web server to serve the frontend and reverse proxy requests to the backend.

## Setup Instructions

1. **Clone the repository**:

   ```sh
   git clone https://github.com/Ravencodess/devops-stage-2
   cd devops-stage-2
   ```

2. **Build and start the services**:

   ```sh
   docker compose up -d
   ```

3. **Verify the services are running**:
   - **FastAPI Backend**: [http://localhost/api](http://localhost/api)
   - **Node.js Frontend**: [http://localhost](http://localhost)
   - **PostgreSQL Database**: Accessible on port `5432` (no direct browser access)
   - **Adminer**: [http://localhost:8080](http://localhost:8080) or [http://db.localhost](http://db.localhost)
   - **Nginx Proxy Manager**: [http://localhost:8090](http://localhost:8090) or [http://proxy.localhost](http://proxy.localhost)

## Service Details

### Backend (FastAPI)

- **Directory**: `./backend`
- **Docker Container**: `fastapi_app`
- **Port**: `8000`
- **Environment Variables**:
  - `POSTGRES_SERVER`: Hostname of the PostgreSQL server.
  - `POSTGRES_PASSWORD`: Password for the PostgreSQL user.

### Frontend (Node.js)

- **Directory**: `./frontend`
- **Docker Container**: `nodejs_app`
- **Port**: `5173`
- **Environment Variables**:
  - `VITE_API_URL`: URL of the backend API.

### Database (PostgreSQL)

- **Docker Image**: `postgres:latest`
- **Docker Container**: `postgres_db`
- **Port**: `5432`
- **Environment Variables**:
  - `POSTGRES_USER`: Username for PostgreSQL.
  - `POSTGRES_PASSWORD`: Password for the PostgreSQL user.
  - `POSTGRES_DB`: Name of the PostgreSQL database.
- **Volumes**:
  - `postgres_data`: Persists PostgreSQL data.

### Adminer

- **Docker Image**: `adminer`
- **Docker Container**: `adminer`
- **Port**: `8080`

### Proxy (Nginx Proxy Manager)

- **Docker Image**: `jc21/nginx-proxy-manager:latest`
- **Docker Container**: `nginx_proxy_manager`
- **Port**: `8090`
- **Volumes**:
  - `./data`: Persistent data for the proxy manager.
  - `./letsencrypt`: SSL certificates.

### Nginx

- **Docker Image**: `nginx:latest`
- **Docker Container**: `nginx`
- **Port**: `80`
- **Volumes**:
  - `./nginx.conf`: Configuration file for Nginx.
  - `./proxy_params.conf`: Proxy parameters for Nginx.
- **Depends On**:
  - `frontend`
  - `backend`
  - `db`
  - `adminer`
  - `proxy`

## Accessing the Application

- **Localhost**: You can access the application via `http://localhost`.
- **Custom Domain**: You can set up your domain to connect to the application using the Nginx Proxy Manager.
