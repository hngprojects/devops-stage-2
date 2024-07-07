# Stage 1: Build the application
FROM node:alpine AS build

WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the application code and build the application
COPY . .
RUN npm run build

# Stage 2: Production-ready image
FROM node:alpine

WORKDIR /usr/src/app

# Copy package.json and package-lock.json for production dependencies
COPY --from=build /usr/src/app/package.json /usr/src/app/package-lock.json ./
RUN npm install

# Copy the build output to the production image
COPY --from=build /usr/src/app/public ./public
COPY . .

# Expose the port that the application will run on
EXPOSE 3000

# Command to run the application
CMD ["npm", "run", "dev"]