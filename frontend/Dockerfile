FROM node:latest

WORKDIR /user/src/app

COPY package*.json ./

COPY . /user/src/app

RUN npm install

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]