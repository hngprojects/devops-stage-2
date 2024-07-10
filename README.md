# Full-Stack FastAPI and React Template

Welcome to the Full-Stack FastAPI and React template repository. This repository serves as a demo application for interns, showcasing how to set up and run a full-stack application with a FastAPI backend and a ReactJS frontend using ChakraUI.

## Project Structure

The repository is organized into two main directories:

- **frontend**: Contains the ReactJS application.
- **backend**: Contains the FastAPI application and PostgreSQL database integration.

Each directory has its own README file with detailed instructions specific to that part of the application.

## Getting Started

To get started with this template, please follow the instructions in the respective directories:

- [Frontend README](./frontend/README.md)
- [Backend README](./backend/README.md)

## Creating the image
- To start the service, "cd" into the web-app-dockerizing directory and run command. Note: ensure that the docker and docker-compose is installed on your machine

*Note:*
- *ensure that docker and docker-compose have been properly installed on your system*
- *Ensure you add the current loggedin user to docker group so you don't have to use sudo all the time in running docker-compose or docker*

```bash
docker-compose up -d
```

## The deployed app
- Access the deployed app on: **www.cadaservices.tech**
- Access the deployed adminer on: **db.cadaservices.tech**
- Access the deployed traefik on: **proxy.cadaservices.tech**