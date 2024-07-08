FROM node:18-alpine
WORKDIR /var/www/app
COPY package*.json ./
RUN npm install
COPY . .
COPY .env .env
EXPOSE 5173
CMD ["npm", "run", "dev"]