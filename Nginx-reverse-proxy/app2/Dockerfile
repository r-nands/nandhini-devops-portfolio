# app2/Dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . /app
RUN npm init -y && npm install express
EXPOSE 3000
CMD ["node", "app.js"]