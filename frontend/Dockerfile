# Use the official Node.js image to build the React app
FROM node:16 AS build

# Set the working directory
WORKDIR /app

#Copy to working directory
COPY . .

# Install dependencies
RUN npm install

# Build the React app
RUN npm run build

# Use the official Nginx image to serve the built app
FROM nginx:alpine

# Copy the built React app from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]