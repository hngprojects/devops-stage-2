# Frontend - ReactJS with ChakraUI

This directory contains the frontend of the application built with ReactJS and ChakraUI.

## Prerequisites

- Node.js (version 14.x or higher)
- npm (version 6.x or higher)

## Setup Instructions

 **Navigate to the frontend directory**:
    ```sh
    cd frontend
    ```

**Install dependencies**:
    ```sh
    npm install
    ```

**Run the development server**:
    ```sh
    npm run dev
    ```

**testing the application using curl**
```sh
curl localhost:5173
```

**testing the application using a web browser locally**
```sh
http://<your_domain_name-or-your_machine_ip>:5173
```

**Configure API URL**:
- navigate to the .env file in the frontend root folder and change the VITE_API_URL to point to you domain name instead of localhost:
```sh
VITE_API_URL=http://<your_domain_name>
```