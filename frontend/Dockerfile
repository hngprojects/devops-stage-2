#Use the latest node image to build
FROM node:latest


#set the working directory
WORKDIR /user/src/app


#Copy the dependencies
COPY package*.json ./


#copy the project folder to the working directory
COPY . /user/src/app

#install dependencies
RUN npm install


#expose port
EXPOSE 5173


#Start the app
CMD ["npm", "run", "dev", "--", "--host"]