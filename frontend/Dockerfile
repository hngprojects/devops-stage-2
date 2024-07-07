# Use a specific Node.js version for better consistency
FROM node:20

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if you have it)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Build the Next.js app for production
RUN npm run build

# Expose the port Next.js is expected to run on (usually 3000)
EXPOSE 5173

# Set the working directory to the 'dist' folder
WORKDIR /app/dist

# Start the Next.js server
CMD ["npx", "serve", "-s", "-l", "5173", "-H", "0.0.0.0"]
