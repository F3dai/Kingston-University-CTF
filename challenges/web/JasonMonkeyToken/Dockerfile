FROM node:lts-jessie

# Create app directory
WORKDIR /root/app

COPY src/package.json .
RUN npm install

COPY src/ .

EXPOSE 8080
ENTRYPOINT ["npm", "start"]