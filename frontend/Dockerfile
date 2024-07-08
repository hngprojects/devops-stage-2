# Stage 1: Build the React application
FROM node:18-alpine AS build
# Set the working directory
WORKDIR /app
# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./
# Install dependencies
RUN npm install
# Copy the rest of the application to the working directory
COPY . .
# Build the React application
RUN npm run build
# Stage 2: Serve the React application with Nginx
FROM nginx:alpine
# Remove the default Nginx website
RUN rm -rf /usr/share/nginx/html/*
# Copy the build output to the Nginx HTML directory
COPY --from=build /app/dist /usr/share/nginx/html
# Expose port 80
EXPOSE 80
# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
